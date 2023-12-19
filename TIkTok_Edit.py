import moviepy.editor as mpy
from moviepy.video.fx.all import crop, resize

# Load the videos
clip1 = mpy.VideoFileClip("video1.mp4")
clip2 = mpy.VideoFileClip("video2.mp4")

# Function to crop and resize a clip
def crop_and_resize(clip, target_width, target_height):
    # Calculate crop dimensions
    original_width, original_height = clip.size
    start_x = (original_width - target_width) // 2
    cropped_clip = crop(clip, x1=start_x, y1=0, x2=start_x + target_width, y2=original_height)

    # Resize the cropped clip
    resized_clip = resize(cropped_clip, newsize=(target_width, target_height))
    return resized_clip

# New dimensions
new_width = 1080
new_height_per_clip = 1920 // 2

# Crop and resize each clip
resized_clip1 = crop_and_resize(clip1, new_width, new_height_per_clip)
resized_clip2 = crop_and_resize(clip2, new_width, new_height_per_clip)

# Combine the clips in a column
combined_clip = mpy.clips_array([[resized_clip1], [resized_clip2]])

# Write the resulting video to a file
combined_clip.write_videofile("combined_video.mp4")

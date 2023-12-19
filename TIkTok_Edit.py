import moviepy.editor as mpy
from moviepy.video.fx.all import crop, resize

# Fonction pour cropper et redimensionner un clip
def process_clip(filename):
    clip = mpy.VideoFileClip(filename)

    # Redimensionner pour que la hauteur soit de 960 pixels tout en conservant les proportions
    resized_clip = resize(clip, height=960)

    # Calculer la largeur après le redimensionnement et cropper pour obtenir 1080px de large
    (w, h) = resized_clip.size
    if w > 1080:
        x1, x2 = (w - 1080) // 2, (w + 1080) // 2
        cropped_clip = crop(resized_clip, x1=x1, y1=0, x2=x2, y2=h)
    else:
        cropped_clip = resized_clip

    return cropped_clip


# Traitement des deux clips
resized_clip1 = process_clip("video1.mp4")
resized_clip2 = process_clip("video2.mp4")

# Combinaison des clips en une colonne
combined_clip = mpy.clips_array([[resized_clip1], [resized_clip2]])

# Écriture du clip final
combined_clip.write_videofile('combined_video.mp4')

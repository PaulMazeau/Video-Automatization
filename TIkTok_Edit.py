import moviepy.editor as mpy
from moviepy.video.fx.all import crop, resize
import random

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

# Durée minimale des deux clips
min_duration = min(resized_clip1.duration, resized_clip2.duration)

# Couper les clips à la durée minimale
resized_clip1 = resized_clip1.subclip(0, min_duration)
resized_clip2 = resized_clip2.subclip(0, min_duration)

# Combinaison des clips en une colonne
combined_clip = mpy.clips_array([[resized_clip1], [resized_clip2]])

# Découpage et exportation des segments avec durée aléatoire
current_time = 0
part = 1
while current_time < min_duration:
    # Durée aléatoire du segment entre 61 et 90 secondes
    segment_duration = random.randint(61, 90)

    # Calculer le temps de fin du segment
    end_time = current_time + segment_duration

    # S'assurer que le temps de fin ne dépasse pas la durée totale de la vidéo
    if end_time > combined_clip.duration:
        end_time = combined_clip.duration

    # Découper le segment
    segment = combined_clip.subclip(current_time, end_time)

    # Exporter le segment
    segment.write_videofile(f'combined_video_part_{part}.mp4')

    # Mettre à jour le temps de début pour le prochain segment et incrémenter le compteur de partie
    current_time = end_time
    part += 1

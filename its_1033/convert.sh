# To convert the original to a cropped mp4
#ffmpeg -y -i its_1033_orig.mp4 -ss 00:00:12.000 -to 00:00:29.500 its_1033_cropped.mp4

# Convert the .srt to .ass for use with -vf
ffmpeg -y -i subtitle.srt subtitle.ass

# Combine subtitles and mp4 (with audio)
ffmpeg -y -i its_1033_cropped.mp4 -vf ass=subtitle.ass its_1033_final.mp4

# Combine subtitles and mp4 (without audio)
ffmpeg -y -i its_1033_cropped.mp4 -an -vf ass=subtitle.ass its_1033_final_nosound.mp4

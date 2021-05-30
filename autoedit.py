from re import split
from moviepy.editor import VideoFileClip,CompositeVideoClip,ImageClip,concatenate_videoclips
from moviepy.video.fx.all import mask_color,fadeout
from moviepy.audio.fx.all import audio_fadein,audio_fadeout

#manually decide start time and end time
starmin,startsec = input("start time in min,sec:").split(",") #01,01
endmin,endsec = input("end time in min,sec:").split(",") #04,11
icon_path = input("icon_path:")
starmin = int(starmin)
startsec = int(startsec)
endmin = int(endmin)
endsec = int(endsec)

'''
starmin = 1
startsec = 1
endmin = 2
endsec = 1
icon_path = ""
'''

# load video source
fire = VideoFileClip("./fire.m4v")
masked_fire = mask_color(fire,color=[0,0,0],thr = 50) #filter black background
show = VideoFileClip("./back.mp4").subclip((starmin,startsec),(endmin,endsec))

# add freeze title
title_bg = show.to_ImageClip(t=0, with_mask=True, duration= fire.duration) #freeze show background
masked_fire = masked_fire.resize(title_bg.size)
title = CompositeVideoClip([title_bg,masked_fire.set_position("center")], use_bgclip=False)

#fade in audio
show = audio_fadein(show,5)

# use icon img or middle frame of animate
if icon_path:
    icon = ImageClip(icon_path).set_duration(show.duration - 3)
else:
    icon = masked_fire.to_ImageClip(t= fire.duration / 2, with_mask=True, duration= show.duration - 3)
#add icon to corner

icon = icon.crossfadein(3)
icon = icon.crossfadeout(3)
icon = icon.resize(width=256)
show_with_icon = CompositeVideoClip([show,icon.set_position(("left","bottom"))], use_bgclip=False)

#final concat
final_clip = concatenate_videoclips([title,show_with_icon])

#final fadeout
final_clip = audio_fadeout(final_clip,5)
final_clip = fadeout(final_clip,3)

#write final clip
final_clip.write_videofile("test.mp4", fps=30)
final_clip.close()
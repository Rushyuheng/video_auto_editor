from re import split
from moviepy.editor import VideoFileClip,CompositeVideoClip,ImageClip,concatenate_videoclips
from moviepy.video.fx.all import mask_color,fadeout
from moviepy.audio.fx.all import audio_fadein,audio_fadeout
def getvideolength(filename):
    video = VideoFileClip(filename)
    min = int(int(video.duration) / 60)
    sec = int(video.duration) % 60
    return min,sec

def writevideo(index,show_filename,start_time,end_time,animate_filename,enable_blackfilter,icon_filename,icon_pos,icon_size,genicon):
    # load video source
    fire = VideoFileClip(animate_filename)
    if enable_blackfilter:
        masked_fire = mask_color(fire,color=[0,0,0],thr = 50) #filter black background
    else:
        masked_fire = fire
    show = VideoFileClip(show_filename).subclip((start_time),(end_time))

    # add freeze title
    title_bg = show.to_ImageClip(t=0, with_mask=True, duration= fire.duration) #freeze show background
    masked_fire = masked_fire.resize(title_bg.size).crossfadeout(3)
    title = CompositeVideoClip([title_bg,masked_fire.set_position("center")], use_bgclip=False)

    #fade in audio
    show = audio_fadein(show,5)
    
    if icon_filename or genicon:
        # use icon img or middle frame of animate
        if icon_filename:
            icon = ImageClip(icon_filename).set_duration(show.duration - 3)
        elif genicon:
            icon = masked_fire.to_ImageClip(t= fire.duration / 2, with_mask=True, duration= show.duration - 3)
        #add icon to corner
        icon = icon.crossfadein(3)
        icon = icon.crossfadeout(3)
        icon = icon.resize(icon_size)
        show = CompositeVideoClip([show,icon.set_position(icon_pos)], use_bgclip=False)

    #final concat
    final_clip = concatenate_videoclips([title,show])

    #final fadeout
    final_clip = audio_fadeout(final_clip,5)
    final_clip = fadeout(final_clip,3)

    #write final clip
    final_clip.write_videofile("result_" + str(index) + ".mp4", fps=30)
    final_clip.close()
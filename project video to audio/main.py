import moviepy
import moviepy.editor
from  tkinter.filedialog import askopenfilename,asksaveasfilename
video = moviepy.editor.VideoFileClip(askopenfilename(title="Select Video File",filetypes=(("mp4 video file",".mp4"),("all files","*.*"))))
audio = video.audio
audio.write_audiofile(asksaveasfilename(title="Audio File Save",filetypes=(("mp3 audio file",".mp3"),("all files","*.*"))))
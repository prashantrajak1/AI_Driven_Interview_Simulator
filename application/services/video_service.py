# from moviepy import VideoFileClip
# import os

# class VideoService:
#     @staticmethod
    
#     def extract_audio(video_path: str) -> str:
#         try:
#             print(f"[INFO] Extracting audio from: {video_path}")
#             video = VideoFileClip(video_path)
            
#             if not video.audio:
#                 print("No audio track found in video.")
                
#             if video.duration is None or video.duration == 0:
#                 raise ValueError("Video duration is not detectable")
            
#             audio_path = video_path.rsplit('.',1)[0] + ".mp3"
#             video.audio.write_audiofile(audio_path, codec = 'lipmp3lame', ffmpeg_params = ["-vn"])
#             print(f"[SUCCESS] Audio saved to: {audio_path}")
#             return audio_path
#         except Exception as e:
#             print("Error failed to extract audio : ", str(e))


import subprocess
import os

class VideoService:
    @staticmethod
    def extract_audio(video_path: str) -> str:
        try:
            print(f"[INFO] Extracting audio from: {video_path}")
            audio_path = os.path.splitext(video_path)[0] + ".mp3"

            command = [
                "ffmpeg",
                "-y",  # Overwrite output file if exists
                "-i", video_path,
                "-vn",  # Disable video
                "-acodec", "libmp3lame",  # Encode audio to MP3
                audio_path
            ]

            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if result.returncode != 0:
                print(f"[ERROR] ffmpeg error:\n{result.stderr.decode()}")
                return None

            print(f"[INFO] Audio successfully saved at: {audio_path}")
            return audio_path

        except Exception as e:
            print(f"[ERROR] Exception while extracting audio: {e}")
            return None

from app.services.video_service import start_video_detection

# 🎥 VIDEO DOSYASI (ANA SENARYO)
start_video_detection("traffic.mp4")

# 💻 WEBCAM (istersen aç)
# start_video_detection(0)

# 📱 TELEFON KAMERASI (IP Camera App ile)
# start_video_detection("http://192.168.1.5:8080/video")
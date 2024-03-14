from moviepy.editor import VideoFileClip

def convert_avi_to_mp4(avi_file_path, output_mp4_file_path):
    # AVI 파일 로드
    clip = VideoFileClip(avi_file_path)
    
    # MP4로 변환하여 저장
    clip.write_videofile(output_mp4_file_path)

# 변환 실행 예시
avi_file_path = 'avi_sample.mov'  # 변환할 AVI 파일 경로
output_mp4_file_path = 'output_avi_to_mp4.mp4'  # 결과 MP4 파일 경로

convert_avi_to_mp4(avi_file_path, output_mp4_file_path)

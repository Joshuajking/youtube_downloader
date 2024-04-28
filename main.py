import os
from pytube import YouTube


def download(link, output_dir):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    output = os.path.join(output_dir, youtubeObject.title)
    try:
        youtubeObject.download(output_path=output)
    except Exception as e:
        print(f"An error has occurred {str(e)}")
    print("Download is completed successfully")


if __name__ == "__main__":
    link = input("Enter the YouTube video URL: ")
    videos_dir = os.path.expanduser("~/Videos")
    download(link, videos_dir)

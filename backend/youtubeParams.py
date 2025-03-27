ydl_opts = {
    'video': {
        'format': 'bestvideo',
        'noplaylist': False,  # Download single video if URL is part of a playlist
        'quiet': False,  # Show download progress in the console
        'ignoreerrors': True,  # Continue even if an error is encountered
        'no_warnings': True,  # Suppress warnings
    },
    'audio': {
        'format': 'bestaudio/best',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            },
            {
                'key': 'FFmpegMetadata',
            },
        ],
        'writethumbnail': False,  # Download thumbnail if available
        'embedthumbnail': True,  # Embed the thumbnail into the MP3 file
        'ignoreerrors': True,  # Continue processing even if some errors occur
    }
}

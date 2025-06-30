import os
import yt_dlp
import logging
from flask_cors import CORS
from flask import Flask, request, jsonify
from youtubeParams import ydl_opts

DOWNLOAD_FOLDER = '/downloads'
logs_folder = '/config'
logging.basicConfig(
    filename=os.path.join(logs_folder, 'ytdownload.log'),
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

app = Flask(__name__)
CORS(app)

AUDIO_FOLDER = os.path.join(DOWNLOAD_FOLDER, 'YT audios')
VIDEO_FOLDER = os.path.join(DOWNLOAD_FOLDER, 'YT videos')

os.makedirs(AUDIO_FOLDER, exist_ok=True)
os.makedirs(VIDEO_FOLDER, exist_ok=True)

folder_mapping = {
    'audio': AUDIO_FOLDER,
    'video': VIDEO_FOLDER
}


@app.route('/api/download/', methods=['POST'])
def download():
    try:
        data = request.json
        url = data.get('url')
        file_format = data.get('file_formate')

        if not url or not file_format:
            return jsonify({'error': 'Missing required parameters: url or file_formate'}), 400

        param = ydl_opts.get(file_format)
        if not param:
            return jsonify({'error': 'Invalid file format'}), 400

        param['outtmpl'] = os.path.join(folder_mapping[file_format], '%(title)s.%(ext)s')

        try:
            logger.info(f"Starting download: {url} with format: {file_format}")
            with yt_dlp.YoutubeDL(param) as ydl:
                result = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(result)

            logger.info(f"Download complete: {filename}")
            return jsonify({'message': 'Download complete', 'file': filename})
        except yt_dlp.utils.DownloadError as e:
            logger.error(f"Download error: {e}")
            return jsonify({'error': 'Download failed'}), 500
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return jsonify({'error': 'Unexpected error occurred'}), 500
    except Exception as e:
        logger.error(f"Error in request handling: {e}")
        return jsonify({'error': 'Server error'}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)

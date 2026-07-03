from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from dotenv import load_dotenv
from s3_service import s3_service

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        's3_configured': s3_service.is_configured()
    }), 200

# S3 Upload URL generation endpoint
@app.route('/api/upload-url', methods=['POST'])
def get_upload_url():
    """
    Generate a presigned S3 upload URL
    Expected JSON body:
    {
        "filename": "photo.jpg",
        "content_type": "image/jpeg",
        "user_id": "user123",
        "folder": "photos"
    }
    """
    try:
        data = request.get_json()
        
        if not all(k in data for k in ['filename', 'content_type', 'user_id']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        upload_info = s3_service.generate_upload_url(
            filename=data['filename'],
            content_type=data['content_type'],
            user_id=data['user_id'],
            folder=data.get('folder', 'photos')
        )
        
        return jsonify(upload_info), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.error(f"Error generating upload URL: {str(e)}")
        return jsonify({'error': 'Failed to generate upload URL'}), 500

# S3 Download URL generation endpoint
@app.route('/api/download-url', methods=['POST'])
def get_download_url():
    """
    Generate a presigned S3 download URL
    Expected JSON body:
    {
        "s3_key": "photos/user123/file-uuid.jpg",
        "filename": "photo.jpg"
    }
    """
    try:
        data = request.get_json()
        
        if 's3_key' not in data:
            return jsonify({'error': 'Missing s3_key'}), 400
        
        download_url = s3_service.generate_download_url(
            s3_key=data['s3_key'],
            filename=data.get('filename')
        )
        
        return jsonify({'download_url': download_url}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.error(f"Error generating download URL: {str(e)}")
        return jsonify({'error': 'Failed to generate download URL'}), 500

# Delete file endpoint
@app.route('/api/delete-file', methods=['POST'])
def delete_file():
    """
    Delete a file from S3
    Expected JSON body:
    {
        "s3_key": "photos/user123/file-uuid.jpg"
    }
    """
    try:
        data = request.get_json()
        
        if 's3_key' not in data:
            return jsonify({'error': 'Missing s3_key'}), 400
        
        success = s3_service.delete_file(s3_key=data['s3_key'])
        
        if success:
            return jsonify({'message': 'File deleted successfully'}), 200
        else:
            return jsonify({'error': 'Failed to delete file'}), 500
    except Exception as e:
        logger.error(f"Error deleting file: {str(e)}")
        return jsonify({'error': 'Failed to delete file'}), 500

# File metadata endpoint
@app.route('/api/file-metadata', methods=['POST'])
def get_file_metadata():
    """
    Get metadata for a file in S3
    Expected JSON body:
    {
        "s3_key": "photos/user123/file-uuid.jpg"
    }
    """
    try:
        data = request.get_json()
        
        if 's3_key' not in data:
            return jsonify({'error': 'Missing s3_key'}), 400
        
        metadata = s3_service.get_file_metadata(s3_key=data['s3_key'])
        
        if metadata:
            return jsonify(metadata), 200
        else:
            return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        logger.error(f"Error getting file metadata: {str(e)}")
        return jsonify({'error': 'Failed to get file metadata'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

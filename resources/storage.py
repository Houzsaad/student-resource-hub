import cloudinary
from cloudinary_storage.storage import MediaCloudinaryStorage

class PDFCloudinaryStorage(MediaCloudinaryStorage):
    def _upload(self, name, content):
        options = {"resource_type": "image", "use_filename": True, "unique_filename": True}
        options.update(self._get_options(name))
        return cloudinary.uploader.upload(content, **options)
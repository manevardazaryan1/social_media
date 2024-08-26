def upload_image(instance, filename):
    """Upload images function"""
    filename = filename.replace(" ", "_").replace("'", "").replace("-", "")
    return f"post_images/{instance.created_at}_{filename}"
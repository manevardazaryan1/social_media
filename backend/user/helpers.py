def upload_image(instance, filename):
    """Upload images function"""
    filename = filename.replace(" ", "_").replace("'", "").replace("-", "")
    return f"profile_pictures/{instance.user.username}_{filename}"
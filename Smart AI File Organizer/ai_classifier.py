def ai_categorize(filename):

    filename = filename.lower()

    if "invoice" in filename or "bill" in filename:
        return "Finance"

    elif "resume" in filename or "cv" in filename:
        return "Career"

    elif filename.endswith(".jpg") or filename.endswith(".png"):
        return "Images"

    else:
        return "Others"
# Dummy classifier for now

def classify_document(text):
    if "non-disclosure" in text.lower():
        return "NDA"
    elif "lease agreement" in text.lower():
        return "Lease"
    else:
        return "Unknown"

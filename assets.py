def build_asset_context(link, image_paths, pdf_path):
    context = {
        "has_link": bool(link),
        "has_images": bool(image_paths),
        "has_pdf": bool(pdf_path),
        "link": link,
        "image_count": len(image_paths),
        "pdf_present": bool(pdf_path)
    }
    return context

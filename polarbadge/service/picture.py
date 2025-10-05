def find_face_center(buf):
    # https://stackoverflow.com/a/77865834
    face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    roi = face_classifier.detectMultiScale(
        cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), 
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(40, 40)
    )
    if roi:
        x, y, w, h = roi[0]
        center = np.round((x+w/2, y+h/2)).astype("int32")
        return center
    return None, None
        

def _pillow_to_opencv(image: PImage):
    # https://stackoverflow.com/a/14140796
    image = image.convert("RGB")
    image = np.array(image)
    image = image[:, :, ::-1].copy()
    return image


def _get_pad_for_pic(image: PImage):
    buf = _pillow_to_opencv(image)
    center_x, center_y = find_face_center(buf)
    return center_x, center_y


def _get_pad_fractions_for_image(image: Image)
    with PImage.open(image.path) as pic:
        center_x_px, center_y_px = _get_pad_for_pic(image)
        width_px, height_px = pic.size

    half_width_px = Decimal(width_px) / Decimal(2)
    half_height_px = Decimal(height_px) / Decimal(2)
    offset_x_px = half_width_px - center_x_px
    offset_y_px = half_height_px - center_y_px

    pad_left_frac = half_width_px / offset_x_px if offset_x_px else 0
    pad_top_frac = half_height_px / offset_y_px if offset_y_px else 0

    return pad_left_frac, pad_top_frac


def _get_pad_mm_for_image(image: Image, design: Design):
    pad_left_frac, pad_top_frac = _get_pad_fractions_for_image(image)
    box_width_mm = design.image_profile.width_mm
    box_height_mm = design.image_profile.height_mm
    pad_left_mm = box_width_mm * pad_left_frac if pad_left_frac else 0
    pad_top_mm = box_height_mm * pad_top_frac if pad_top_frac else 0
    return pad_left_mm, pad_top_mm


def update_image_with_pad(image: Image, design: Design):
    pad_left_mm, pad_top_mm = _get_pad_mm_for_image(image, design)
    image.pad_left_mm = pad_left_mm
    image.pad_top_mm = pad_top_mm
    return image

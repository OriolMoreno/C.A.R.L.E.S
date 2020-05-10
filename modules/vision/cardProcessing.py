import cv2


def downscale(image):
    # Downscale the image to width 680
    scale_percent = 680 / image.shape[1]
    width = int(image.shape[1] * scale_percent)
    height = int(image.shape[0] * scale_percent)
    dim = (width, height)
    # resize image
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    return image


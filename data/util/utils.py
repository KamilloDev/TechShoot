import pygame

def load_image(image_path):
    img = pygame.image.load('data/images/' + image_path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(images_path):
    images = []
    for image in images_path:
        img = load_image(image)
        img.set_colorkey((0, 0, 0))
        images.append(img)
    return images
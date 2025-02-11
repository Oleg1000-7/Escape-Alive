from pygame import sprite

all_sprites = sprite.Group()
entities = sprite.Group()
interactive = sprite.Group()
moving = sprite.Group()
hud_elements = sprite.Group()

def clear_groups():
    all_sprites.empty()
    entities.empty()
    interactive.empty()
    moving.empty()
    hud_elements.empty()
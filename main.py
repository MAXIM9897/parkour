@namespace
class SpriteKind:
    coin = SpriteKind.create()

def on_overlap_tile(sprite, location):
    game.game_over(True)
    game.set_game_over_effect(True, effects.confetti)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile)

def on_up_pressed():
    if CAT.vy == 0:
        CAT.vy = -175
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_overlap(sprite3, otherSprite):
    info.change_score_by(1)
    sprites.destroy(otherSprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.coin, on_on_overlap)

def on_overlap_tile2(sprite2, location2):
    game.game_over(False)
    game.set_game_over_effect(False, effects.melt)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile2)

CAT: Sprite = None
scene.set_background_color(9)
CAT = sprites.create(assets.image("""
    cat
"""), SpriteKind.player)
controller.move_sprite(CAT, 100, 0)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
CAT.ay = 350
scene.camera_follow_sprite(CAT)
tiles.place_on_random_tile(CAT, assets.tile("""
    myTile2
"""))
coin2 = sprites.create(img("""
        . . . . . . . . . . . . . . . 
            . . . . f f f f f f f . . . . 
            . . . f 5 5 5 5 5 5 5 f . . . 
            . . f 5 5 4 4 4 4 5 5 5 f . . 
            . f 5 5 5 5 5 5 5 5 5 5 5 f . 
            . f 5 4 5 5 5 5 5 5 5 5 5 f . 
            . f 5 4 5 5 5 5 5 5 5 5 5 f . 
            . f 5 4 5 5 5 5 5 5 5 5 5 f . 
            . f 5 4 5 5 5 5 5 5 5 5 5 f . 
            . f 5 4 5 5 5 5 5 5 5 5 5 f . 
            . f 5 4 5 5 5 5 5 5 5 5 5 f . 
            . . f 5 5 4 4 5 5 5 5 5 f . . 
            . . . f 5 5 5 5 5 5 5 f . . . 
            . . . . f f f f f f f . . . . 
            . . . . . . . . . . . . . . .
    """),
    SpriteKind.coin)
for value in tiles.get_tiles_by_type(assets.tile("""
    myTile1
""")):
    tiles.place_on_tile(coin2, value)
    tiles.set_tile_at(value, assets.tile("""
        transparency16
    """))
    animation.run_image_animation(coin2,
        [img("""
                . . . . . . . . . . . . . . . 
                        . . . . f f f f f f f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . 
                        . . f 5 5 4 4 4 4 5 5 5 f . . 
                        . f 5 5 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                        . f 5 4 5 5 5 5 5 5 5 5 5 f . 
                        . . f 5 5 4 4 5 5 5 5 5 f . . 
                        . . . f 5 5 5 5 5 5 5 f . . . 
                        . . . . f f f f f f f . . . . 
                        . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . 
                        . . . . . f f f f f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . 
                        . . . f 5 5 4 4 4 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . 
                        . . f 5 4 5 5 5 5 5 5 5 f . . 
                        . . f 5 4 5 5 5 5 5 5 5 f . . 
                        . . f 5 4 5 5 5 5 5 5 5 f . . 
                        . . f 5 4 5 5 5 5 5 5 5 f . . 
                        . . f 5 4 5 5 5 5 5 5 5 f . . 
                        . . f 5 4 5 5 5 5 5 5 5 f . . 
                        . . . f 5 5 4 5 5 5 5 f . . . 
                        . . . . f 5 5 5 5 5 f . . . . 
                        . . . . . f f f f f . . . . . 
                        . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . 
                        . . . . . . f f f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . 
                        . . . . f 5 5 4 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . 
                        . . . f 5 4 5 5 5 5 5 f . . . 
                        . . . f 5 4 5 5 5 5 5 f . . . 
                        . . . f 5 4 5 5 5 5 5 f . . . 
                        . . . f 5 4 5 5 5 5 5 f . . . 
                        . . . f 5 4 5 5 5 5 5 f . . . 
                        . . . f 5 4 5 5 5 5 5 f . . . 
                        . . . . f 5 5 5 5 5 f . . . . 
                        . . . . . f 5 5 5 f . . . . . 
                        . . . . . . f f f . . . . . . 
                        . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . 
                        . . . . . . . f . . . . . . . 
                        . . . . . . f 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . 
                        . . . . f 5 4 5 5 5 f . . . . 
                        . . . . f 5 4 5 5 5 f . . . . 
                        . . . . f 5 4 5 5 5 f . . . . 
                        . . . . f 5 4 5 5 5 f . . . . 
                        . . . . f 5 4 5 5 5 f . . . . 
                        . . . . f 5 4 5 5 5 f . . . . 
                        . . . . . f 5 5 5 f . . . . . 
                        . . . . . . f 5 f . . . . . . 
                        . . . . . . . f . . . . . . . 
                        . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . 
                        . . . . . . . f . . . . . . . 
                        . . . . . . f 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . 
                        . . . . . f 5 5 5 f . . . . . 
                        . . . . . f 4 5 5 f . . . . . 
                        . . . . . f 4 5 5 f . . . . . 
                        . . . . . f 4 5 5 f . . . . . 
                        . . . . . f 4 5 5 f . . . . . 
                        . . . . . f 4 5 5 f . . . . . 
                        . . . . . f 4 5 5 f . . . . . 
                        . . . . . f 5 5 5 f . . . . . 
                        . . . . . . f 5 f . . . . . . 
                        . . . . . . . f . . . . . . . 
                        . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . 
                        . . . . . . . f . . . . . . . 
                        . . . . . . f 5 f . . . . . . 
                        . . . . . . f 5 f . . . . . . 
                        . . . . . . f 5 f . . . . . . 
                        . . . . . . f 5 f . . . . . . 
                        . . . . . . f 5 f . . . . . . 
                        . . . . . . f 5 f . . . . . . 
                        . . . . . . f 5 f . . . . . . 
                        . . . . . . f 5 f . . . . . . 
                        . . . . . . f 5 f . . . . . . 
                        . . . . . . f 5 f . . . . . . 
                        . . . . . . f 5 f . . . . . . 
                        . . . . . . . f . . . . . . . 
                        . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . 
                        . . . . . . . f . . . . . . . 
                        . . . . . . f 5 f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . 
                        . . . . . f 5 5 5 f . . . . . 
                        . . . . . f 4 5 5 f . . . . . 
                        . . . . . f 4 5 5 f . . . . . 
                        . . . . . f 4 5 5 f . . . . . 
                        . . . . . f 4 5 5 f . . . . . 
                        . . . . . f 4 5 5 f . . . . . 
                        . . . . . f 4 5 5 f . . . . . 
                        . . . . . f 5 5 5 f . . . . . 
                        . . . . . . f 5 f . . . . . . 
                        . . . . . . . f . . . . . . . 
                        . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . 
                        . . . . . . f f f . . . . . . 
                        . . . . . f 5 5 5 f . . . . . 
                        . . . . f 5 5 4 5 5 f . . . . 
                        . . . f 5 5 5 5 5 5 5 f . . . 
                        . . . f 5 4 5 5 5 5 5 f . . . 
                        . . . f 5 4 5 5 5 5 5 f . . . 
                        . . . f 5 4 5 5 5 5 5 f . . . 
                        . . . f 5 4 5 5 5 5 5 f . . . 
                        . . . f 5 4 5 5 5 5 5 f . . . 
                        . . . f 5 4 5 5 5 5 5 f . . . 
                        . . . . f 5 5 5 5 5 f . . . . 
                        . . . . . f 5 5 5 f . . . . . 
                        . . . . . . f f f . . . . . . 
                        . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . 
                        . . . . . f f f f f . . . . . 
                        . . . . f 5 5 5 5 5 f . . . . 
                        . . . f 5 5 4 4 4 5 5 f . . . 
                        . . f 5 5 5 5 5 5 5 5 5 f . . 
                        . . f 5 4 5 5 5 5 5 5 5 f . . 
                        . . f 5 4 5 5 5 5 5 5 5 f . . 
                        . . f 5 4 5 5 5 5 5 5 5 f . . 
                        . . f 5 4 5 5 5 5 5 5 5 f . . 
                        . . f 5 4 5 5 5 5 5 5 5 f . . 
                        . . f 5 4 5 5 5 5 5 5 5 f . . 
                        . . . f 5 5 4 5 5 5 5 f . . . 
                        . . . . f 5 5 5 5 5 f . . . . 
                        . . . . . f f f f f . . . . . 
                        . . . . . . . . . . . . . . .
            """)],
        100,
        True)
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        myTile3
    """)):
        pass
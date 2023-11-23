namespace SpriteKind {
    export const coin = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile0`, function (sprite, location) {
    game.gameOver(true)
    game.setGameOverEffect(true, effects.confetti)
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (CAT.vy == 0) {
        CAT.vy = -175
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.coin, function (sprite3, otherSprite) {
    info.changeScoreBy(1)
    sprites.destroy(otherSprite)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile`, function (sprite2, location2) {
    game.gameOver(false)
    game.setGameOverEffect(false, effects.melt)
})
let CAT: Sprite = null
scene.setBackgroundColor(9)
CAT = sprites.create(assets.image`cat`, SpriteKind.Player)
controller.moveSprite(CAT, 100, 0)
tiles.setCurrentTilemap(tilemap`level1`)
CAT.ay = 350
scene.cameraFollowSprite(CAT)
tiles.placeOnRandomTile(CAT, assets.tile`myTile2`)
let coin = sprites.create(img`
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
    `, SpriteKind.coin)
for (let value of tiles.getTilesByType(assets.tile`myTile1`)) {
    tiles.placeOnTile(coin, value)
    tiles.setTileAt(value, assets.tile`transparency16`)
    animation.runImageAnimation(
    coin,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    true
    )
    for (let value of tiles.getTilesByType(assets.tile`myTile3`)) {
    	
    }
}

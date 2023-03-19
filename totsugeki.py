import pyglet
import imageio
from pyglet.window import Window, WindowException, FPSDisplay

gif_path = "totsugeki.gif"
gif = imageio.mimread(gif_path)
window_width, window_height = 600, 338
config = pyglet.gl.Config(double_buffer=True)
try:
    window = Window(width=window_width, height=window_height, config=config, style=pyglet.window.Window.WINDOW_STYLE_BORDERLESS)
    window.set_location(window.screen.width - window_width, 0)
except WindowException:
    window = Window(width=window_width, height=window_height, config=config)
    window.set_location(window.screen.width - window_width, 0)
window.set_caption("totsugeki")
mp3_path = "totsugeki.mp3"
music = pyglet.media.load(mp3_path)
player = music.play()
player.loop = True
gif_sprite = pyglet.sprite.Sprite(pyglet.image.load_animation(gif_path))
gif_sprite.scale = min(window_width / gif_sprite.width, window_height / gif_sprite.height)
def update(dt):
    gif_sprite.update(dt)
    gif_sprite.draw()
pyglet.clock.schedule_interval(update, 1/60)

pyglet.app.run()
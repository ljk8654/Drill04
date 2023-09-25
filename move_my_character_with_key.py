from pico2d import *


TUK_HEIGHT,TUK_WIDTH = 1280, 1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)


grass = load_image('TUK_GROUND.png')
character = load_image('chracter2.png')

def handle_events():
    global running, x_dir, y_dir, non_event
    global x,left
    events = get_events()
    for event in events:
        non_event = True
        if event.type == SDL_QUIT:
                running = False
        elif event.type == SDL_KEYDOWN:
            non_event = False
            if event.key == SDLK_RIGHT:
                left = False
                x_dir += 1
            elif event.key == SDLK_LEFT:
                left = True
                x_dir -= 1
            elif event.key == SDLK_UP:
                y_dir += 1
            elif event.key == SDLK_DOWN:
                y_dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                x_dir -= 1
            elif event.key == SDLK_LEFT:
                x_dir += 1
            elif event.key == SDLK_UP:
                y_dir -= 1
            elif event.key == SDLK_DOWN:
                y_dir += 1

def line_check():
    global x, y
    if x > 1024- 30:
        x -= 5
    elif x < 30:
        x += 5
    if y > 1280 - 250:
        y -= 5
    elif y < 300:
        y += 5

running = True
x, y = TUK_WIDTH//2,TUK_HEIGHT//2
x_dir, y_dir = 0, 0
x_frame, y_frame, stop_frame = 0, 0, 0
non_event = False
left = True
while running:
    clear_canvas()
    grass.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    if non_event == False:
        if y_frame == 5:
            y_frame=0
        if left == False:
            character.clip_draw(x_frame * 72, y_frame * 85, 68,  85, x, y)
        else:
            character.clip_composite_draw(x_frame * 72, y_frame * 85, 68, 85, 0,'h',x, y,68,85)
        update_canvas()
        handle_events()
        x_frame = (x_frame + 1) % 7
        if x_frame == 0:
            y_frame = (y_frame + 1) % 2
        x += x_dir * 5
        y += y_dir * 5
        line_check()
    elif non_event == True:
        if y_frame != 5:
            y_frame = 5
        if left == True:
            character.clip_composite_draw(stop_frame * 57, y_frame * 85, 57, 85, 0,'h',x, y,57,85)
        else:
            character.clip_draw(stop_frame * 57, y_frame * 85, 57, 85, x, y)
        update_canvas()
        handle_events()
        stop_frame = (stop_frame + 1) % 8
        y_frame = 5
    delay(0.05)

close_canvas()

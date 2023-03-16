import cv2 as cv
import numpy as np

def mouse_event_handler(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        param[0] = True
        param[1] = (x, y)
    elif event == cv.EVENT_LBUTTONUP:
        param[0] = False
    elif event == cv.EVENT_MOUSEMOVE and param[0]:
        param[1] = (x, y)

def free_drawing(canvas_width=1280, canvas_height=720, init_brush_radius=3):
    canvas = np.full((canvas_height, canvas_width, 3), 255, dtype=np.uint8)
    palette = [(0, 0, 0), (255, 255, 255), (0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

    mouse_state = [False, (-1, -1)]
    brush_color = 0
    brush_radius = init_brush_radius
    
    cv.namedWindow('Simple Painting Tool')
    cv.setMouseCallback('Simple Painting Tool', mouse_event_handler, mouse_state)

    while True:
        mouse_left_button_click, mouse_xy = mouse_state
        if mouse_left_button_click:
            cv.circle(canvas, mouse_xy, brush_radius, palette[brush_color], -1)

        canvas_copy = canvas.copy()
        info = f'Brush Radius: {brush_radius}'
        cv.putText(canvas_copy, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (127, 127, 127), thickness=2)
        cv.putText(canvas_copy, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, palette[brush_color])
        cv.imshow('Simple Painting Tool', canvas_copy)

        key = cv.waitKey(1)
        if key == 27:
            break
        elif key == ord('\t'):
            brush_color = (brush_color + 1) % len(palette)
        elif key == ord('=') or key == ('+'):
            brush_radius += 1
        elif key == ord('-') or key == ('_'):
            brush_radius = max(brush_radius - 1, 1)

    cv.destroyAllWindows()

if __name__ == '__main__':
    free_drawing()

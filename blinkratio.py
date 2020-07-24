import distance as dist
import midpoint as mid

def blinkratio_calc(eye_points, landmarks):
    
    corner_left  = (landmarks.part(eye_points[0]).x, landmarks.part(eye_points[0]).y)
    corner_right = (landmarks.part(eye_points[3]).x, landmarks.part(eye_points[3]).y)    
    center_top    = mid.midpoint_calc(landmarks.part(eye_points[1]), landmarks.part(eye_points[2]))
    center_bottom = mid.midpoint_calc(landmarks.part(eye_points[5]), landmarks.part(eye_points[4]))

    horizontal_length = dist.distance_calc(corner_left , corner_right)
    vertical_length = dist.distance_calc(center_top , center_bottom)

    ratio = horizontal_length / vertical_length

    return ratio
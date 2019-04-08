from sciency.mathy import vector

def get_disp_vector(pos_vector_1, pos_vector_2):
    disp_vector = vector.subtract_vectors(pos_vector_1, pos_vector_2)
    return disp_vector

def get_avg_vel_vector(disp_vector, time_taken):
    x, y, z = disp_vector.getX(), disp_vector.getY(), disp_vector.getZ()
    avg_vel_vector = vector.Vector((x/time_taken), (y/time_taken), (z/time_taken))
    return avg_vel_vector

def get_avg_speed(total_distance, time_taken):
    avg_speed = total_distance/time_taken
    return avg_speed

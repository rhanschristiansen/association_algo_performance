from src.util.transform import Transform

class LIDAR_detection():
    def __init__(self, frame, seg, dist, ampl):
        tr = Transform()
        self.frame = frame
        self.dist = dist
        self.seg = seg
        self.bb = tr.lidar_dist_seg_to_bb(dist, seg)
        self.ampl = ampl


print('import succes') 

class wood_structural():
    def __init__(self, length, width, depth, db_id):
        self.length = length
        self.width = width
        self.depth = depth
        self.id = db_id
        
    def print_data(self):
        print(self.length, self.width, self.depth, self.id)


class wood_substructure(wood_structural):
    pass


class wood_cladding():
    def __init__(self, length, height, depth, db_id):
        self.length = length
        self.height = height
        self.depth = depth
        self.id = db_id


class coordinates_segments():
    def __init__(self, x_cor_start, z_cor_start, x_cor_end, z_cor_end):
        self.x_cor_start = x_cor_start
        self.z_cor_start = z_cor_start
        self.x_cor_end = x_cor_end
        self.z_cor_end = z_cor_end
        
    def print_cor(self):
        print(self.x_cor_start, self.z_cor_start, self.x_cor_end, self.z_cor_end)


class coordinates_segments_cladding(coordinates_segments):
    pass
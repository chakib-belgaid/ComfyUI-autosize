
import math

def get_closest_size(canditates, width, height):
    """ get the approximation with the closest ratio"""
    ratio = round(width/height, 3)
    ratio_candidates = sorted(canditates.keys(),reverse=True)
    res = ratio_candidates[0]
    while ratio <= res:
        res = ratio_candidates.pop(0)
    return canditates[res]


class SDXLAutoSize:
    sdxl_sizes = [(1024 , 1024),(2048 , 512),(1920 , 512),(1600 , 640),(1536 , 640),(1472 , 704),(1344 , 768),(960 , 1024),(896 , 1152),(832 , 1216),(768 , 1280),(704 , 1408),(640 , 1536)]
    sdxl_sizes = {round(x/y, 3):(x,y) for x, y in sdxl_sizes}
   
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":{
               "image":("IMAGE", ),
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    
    FUNCTION = "get_size"
    CATEGORY = "Image Size"
    
    def get_size(self, image):
        return get_closest_size(self.sdxl_sizes, image.shape[2], image.shape[1])

class CustomAutoSize:
   
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":{
               "image":("IMAGE", ),
               "latent_size":( "INT",{"default":1048576}),
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    
    FUNCTION = "get_size"
    CATEGORY = "Image Size"
    
    def resize(self,width,hight,latent=1048576):
        old_ratio = math.sqrt(latent / (width * hight))
        old_ratio = math.floor(old_ratio*1000)/1000  # round down to 3 decimal places
        width =math.floor(width*old_ratio)
        hight = math.floor(hight*old_ratio)
        return width,hight
    
    def get_size(self, image, latent_size):
        return self.resize(image.shape[2], image.shape[1], latent_size)
        
        



NODE_CLASS_MAPPINGS = {
    "SDXLAutoSize": SDXLAutoSize,
    "CustomAutoSize": CustomAutoSize
}


NODE_DISPLAY_NAME_MAPPINGS = {
    "SDXLAutoSize": "Auto size for SDXL",
    "CustomAutoSize": "Custom auto size"
}

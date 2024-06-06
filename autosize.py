


class Autosize:

    models = ["sdxl","others"]
    sdxl_sizes = [(1024 , 1024),(2048 , 512),(1920 , 512),(1600 , 640),(1536 , 640),(1472 , 704),(1344 , 768),(960 , 1024),(896 , 1152),(832 , 1216),(768 , 1280),(704 , 1408),(640 , 1536)]
    sdxl_sizes = {round(x/y, 3):(x,y) for x, y in sdxl_sizes}
   
    
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":{ 
               "image":("IMAGE", ),
               "model" : (cls.models, {"default": "sdxl"})
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")

    FUNCTION = "get_size"

    # OUTPUT_NODE = False

    CATEGORY = "Get size"

    def get_closest_size(self,canditates, width, height):
        """ get the approximation with the closest ratio"""
        ratio = round(width/height, 3)
        ratio_candidates = sorted(canditates.keys(),reverse=True)
        res = ratio_candidates[0]
        while ratio <= res:
            res = ratio_candidates.pop(0)
        return canditates[res]
    
    def get_size(self, image, model):
        """ get the size of the image"""
        if model == "sdxl":
            
            return self.get_closest_size(self.sdxl_sizes, image.shape[2], image.shape[1])
        return (image.shape[2], image.shape[1])
    
    # @classmethod
    # def IS_CHANGED(cls, image, string_field, int_field, float_field, print_to_screen):
    #    return ""


NODE_CLASS_MAPPINGS = {
    "Autosize": Autosize
}


NODE_DISPLAY_NAME_MAPPINGS = {
    "Autosize": "Auto size"
}

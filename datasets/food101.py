import os

from .utils import Datum, DatasetBase, read_json, write_json, build_data_loader
from .oxford_pets import OxfordPets


template = ['a photo of {}, a type of food.']
negative_template = ['a photo without {}, a type of food.']

class Food101(DatasetBase):

    dataset_dir = 'food-101'

    def __init__(self, root, num_shots):
        self.dataset_dir = os.path.join(root, self.dataset_dir)
        self.image_dir = os.path.join(self.dataset_dir, 'images')
        self.split_path = os.path.join(self.dataset_dir, 'split_zhou_Food101.json')
        
        self.template = template
        self.negative_template = negative_template
        self.cupl_path = './gpt3_prompts/CuPL_prompts_food101.json'

        train, val, test = OxfordPets.read_split(self.split_path, self.image_dir)
        train = self.generate_fewshot_dataset(train, num_shots=num_shots)

        super().__init__(train_x=train, val=val, test=test)
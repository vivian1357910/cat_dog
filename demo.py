from PIL import Image
import torch
from models.model import MyCNN
from models.model import ExampleCNN
from torchvision import transforms
import os
from tqdm import tqdm
from PIL import Image
import IPython

test_transforms = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

weight_path = "./weights/weight.pth"

# load model and use weights we saved before
#model = ExampleCNN()
model = MyCNN()
model.load_state_dict(torch.load(weight_path, map_location='cpu'))
model = model.to(device)

predict_correct = 0
model.eval()

def demo(img):
  img = test_transforms(img)
  img = img.view(1, 3, 224, 224)
  img = img.to(device)
  output = model(img)
  if(output.data.max(1)[1][0] == 0):
    #print ("It is a CAT.")
    return 'CAT'
  elif(output.data.max(1)[1][0] == 1):
    #print ("It is a DOG.")
    return 'DOG'

'''
img_path = "./data/demo/test1.jpg"
img = Image.open(img_path)
display(img)
demo(img)
'''
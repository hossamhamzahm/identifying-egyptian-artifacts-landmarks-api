#imports
import torch
import torchvision.datasets as datasets # to download dataset form mnisc
import torchvision.transforms as transforms
import os
from PIL import Image
import json

def predict(test_image_name):
    image_transforms =  transforms.Compose([
        transforms.RandomResizedCrop(size=256, scale=(0.8, 1.0)),
        transforms.RandomRotation(degrees=15),
        transforms.RandomHorizontalFlip(),
        transforms.CenterCrop(size=224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225])
    ])

    # Set data directory paths
    # data_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "data_set")
    # class_names = datasets.ImageFolder(root=data_directory, transform=image_transforms).classes

        
    # params_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resnet50_params_egyptian-monuments-and-landmarks_with_02_drop_out")
    # resnet50.load_state_dict(torch.load(params_path,  map_location=torch.device('cpu')))

    # load entire model
    entire_model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resnet50_96acc_modified_data_entire_model.pt")
    model =  torch.jit.load(entire_model_path,  map_location=torch.device('cpu'))


    # obj = {}
    # for idx in range(len(class_names)):
    #     obj[idx] = class_names[idx]
    # print(json.dumps(obj))

    class_names_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "class_name.json")
    class_names = {}

    with open(class_names_directory, "r") as classes_json:
        class_names = json.load(classes_json)


    test_image = Image.open(test_image_name)
    test_image_tensor = image_transforms(test_image)
    prediction = ""
    
    with torch.no_grad():
        # set model in evaluation mode
        model.eval()
        # Model outputs log probabilities
        out = model(test_image_tensor.unsqueeze(0))
        ps = torch.exp(out)
        topk, topclass = ps.topk(1, dim=1)

        test_image.close()
        prediction = class_names[str(int(topclass[0][0]))]

    prediction_data = {"class_name": prediction, "cnn_id": int(topclass[0][0]), "accuracy": float(topk[0][0])}
    if float(topk[0][0]) < 0.7:
        prediction_data = {"class_name": "Unknown", "cnn_id": -1, "accuracy": float(topk[0][0])}

    del model
    print("Output class :  ", prediction)
    return prediction_data
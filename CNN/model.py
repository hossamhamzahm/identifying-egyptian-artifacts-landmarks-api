#imports
import torch
import torchvision.datasets as datasets # to download dataset form mnisc
import torchvision.transforms as transforms
import os
from PIL import Image


def predict(test_image_name):
    image_transforms = { 
        'train': transforms.Compose([
            transforms.RandomResizedCrop(size=256, scale=(0.8, 1.0)),
            transforms.RandomRotation(degrees=15),
            transforms.RandomHorizontalFlip(),
            transforms.CenterCrop(size=224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406],
                                [0.229, 0.224, 0.225])
        ]),
        'valid': transforms.Compose([
            transforms.Resize(size=256),
            transforms.CenterCrop(size=224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406],
                                [0.229, 0.224, 0.225])
        ]),
        'test': transforms.Compose([
            transforms.Resize(size=256),
            transforms.CenterCrop(size=224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406],
                                [0.229, 0.224, 0.225])
        ])
    }
    
    entire_model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entire_model")
    model = torch.load(entire_model_path)
        
    # params_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "params_with_02_drop_out")

    # Set data directory paths
    # data_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)),"data_set", "low_accuracy_many_classes")
    data_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "classes")


    # class_names = datasets.ImageFolder(root=data_directory, transform=image_transforms['train']).classes
    class_names = ['Abu_el-Abbas_el-Mursi_Mosque', 'Agiba_beach', 'Amr ibn Al-Aas Mosque', 'Babylon Fortress', 'Bent pyramid for senefru', 'Bibliotheca_Alexandrina', 'Egyptian Museum Tahrir', 'Great_Hypostyle_Hall_of_Karnak', 'Great_Pyramids_of_Giza', 'Hanging church', 'Mosque_of_al-Mahmudiya', 'Muizz_Street', 'Nefertiti', 'Pyramid_of_Djoser', 'sphinx']

    # Number of classes
    num_classes = len(class_names)

    transform = image_transforms['test']
    test_image = Image.open(test_image_name)
#     plt.imshow(test_image)
    test_image_tensor = transform(test_image)
    prediction = ""
    
    with torch.no_grad():
        model.eval()
        # Model outputs log probabilities
        out = model(test_image_tensor.unsqueeze(0))
        ps = torch.exp(out)
        topk, topclass = ps.topk(1, dim=1)

        test_image.close()
        prediction = class_names[topclass.cpu().numpy()[0][0]]

    del model
    print("Output class :  ", prediction)
    return prediction

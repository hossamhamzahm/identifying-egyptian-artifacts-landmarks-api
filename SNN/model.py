import os
import torch
from PIL import Image
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torch import optim
import torch.nn.functional as F





# Define the Contrastive Loss Function
class ContrastiveLoss(torch.nn.Module):
    def __init__(self, margin=2.0):
        super(ContrastiveLoss, self).__init__()
        self.margin = margin

    def forward(self, output1, output2, label):
      # Calculate the euclidian distance and calculate the contrastive loss
      euclidean_distance = F.pairwise_distance(output1, output2, keepdim = True)

      loss_contrastive = torch.mean((1-label) * torch.pow(euclidean_distance, 2) +
                                    (label) * torch.pow(torch.clamp(self.margin - euclidean_distance, min=0.0), 2))


      return loss_contrastive


# Resize the images and transform to tensors
transformation = transforms.Compose([transforms.Resize((100,100)),
    transforms.ToTensor()
])


# Load the training dataset
feat_vec_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "feat_vec")
feat_vec_folder =  datasets.ImageFolder(root=feat_vec_directory, transform=transformation)
feat_vec_dataloader = DataLoader(feat_vec_folder, shuffle=True, batch_size=1)

class_names = feat_vec_folder.classes
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


params_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "snn_v1_100acc_epoch_50")
entire_model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "snn_entire_model.pt")
# net.load_state_dict(torch.load(params_path, map_location=torch.device(device)))

net = torch.jit.load(entire_model_path,  map_location=torch.device('cpu'))
net.eval()


criterion = ContrastiveLoss()
optimizer = optim.Adam(net.parameters(), lr = 0.0005)
db = []


def predict(test_image_path):
    if len(db) == 0: generate_feature_vectors()

    test_image = Image.open(test_image_path)
    test_image_tensor = transformation(test_image)
    prediction = "Unrecognized"
    
    with torch.no_grad():
        net.eval()
        output1 = net.forward_once(test_image_tensor)

        mi = (200, None)
    for (output2, label) in db:
        euclidean_distance = F.pairwise_distance(output1, output2)

        if euclidean_distance.item() < mi[0]:
            mi = (euclidean_distance.item(), label)

        test_image.close()

    if mi[0] < 0.8: prediction = mi[1]
    print("Output class :  ", prediction)
    return prediction



def generate_feature_vectors():
    all_documents = []
    
    for (x, y) in feat_vec_dataloader:
        label = class_names[y[0]]
        feature_vec = net.forward_once(x.to(device))

        
        doc = {
            "class_name": label,
            "type": "Landmark",
            "name": "Description",
            "vector": feature_vec
        }
        db.append((feature_vec, label))

        all_documents.append(doc)
#Dataset
Both images from google or imageNet are available for this part, as classification only need labelled images without annotation infromation.
#Training
python train.py --dataset dataset --model snake.model --labelbin lb.pickle
#Test
python classify.py --model snake.model --labelbin lb.pickle --image examples/boa.jpg
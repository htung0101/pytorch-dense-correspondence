import dense_correspondence_manipulation.utils.utils as utils
utils.add_dense_correspondence_to_python_path()
from dense_correspondence.training.training import *
import sys
import logging
import argparse

#utils.set_default_cuda_visible_devices()
utils.set_cuda_visible_devices([0]) # use this to manually set CUDA_VISIBLE_DEVICES

from dense_correspondence.training.training import DenseCorrespondenceTraining
from dense_correspondence.dataset.spartan_dataset_masked import SpartanDataset
logging.basicConfig(level=logging.INFO)

from dense_correspondence.evaluation.evaluation import DenseCorrespondenceEvaluation


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--data_name", type=str, default="caterpillar_upright.yaml")
    parser.add_argument("--run_prefix", type=str, default="caterpillar")
    parser.add_argument("--training_yaml", type=str, default="training.yaml")

    args = parser.parse_args()


    config_filename = os.path.join(utils.getDenseCorrespondenceSourceDir(), 'config', 'dense_correspondence', 
                                   'dataset', 'composite', args.data_name)
    config = utils.getDictFromYamlFilename(config_filename)

    train_config_file = os.path.join(utils.getDenseCorrespondenceSourceDir(), 'config', 'dense_correspondence', 
                                   'training', args.training_yaml)

    train_config = utils.getDictFromYamlFilename(train_config_file)
    dataset = SpartanDataset(config=config)
    
    dataset_test = None
    if train_config["training"]["compute_test_loss"]:
        dataset_test=SpartanDataset(mode="test", config=config)

    logging_dir = "trained_models/tutorials"
    #num_iterations = 3500
    d = 3 # the descriptor dimension
    name = f"{args.run_prefix}_%d" %(d)
    train_config["training"]["logging_dir_name"] = name
    train_config["training"]["logging_dir"] = logging_dir
    train_config["dense_correspondence_network"]["descriptor_dimension"] = d
    #train_config["training"]["num_iterations"] = num_iterations


    TRAIN = True
    EVALUATE = True

    if TRAIN:
        print("training descriptor of dimension %d" %(d))
        train = DenseCorrespondenceTraining(dataset=dataset,  dataset_test=dataset_test, config=train_config)
        train.run()
        print("finished training descriptor of dimension %d" %(d))

    model_folder = os.path.join(logging_dir, name)
    model_folder = utils.convert_data_relative_path_to_absolute_path(model_folder)

    if EVALUATE:
        DCE = DenseCorrespondenceEvaluation
        num_image_pairs = 100
        DCE.run_evaluation_on_network(model_folder, num_image_pairs=num_image_pairs)    
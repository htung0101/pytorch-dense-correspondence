


## tutorial from the repo
# visualize data from the code. can run
#python dense_correspondence/dataset/simple_datasets_test.py
#python dense_correspondence/training/training_tutorial.py
#python dense_correspondence/evaluation/evaluation_qualitative_tutorial.py
# visualization
#python modules/user-interaction-heatmap-visualization/live_heatmap_visualization.py




#python dense_correspondence/dataset/simple_datasets_test.py --data_name=open_door_1207_with_images.yaml
#python dense_correspondence/training/training_tutorial.py  --data_name=open_door_1207_with_images.yaml --run_prefix="open_door_1216" --training_yaml=training_door.yaml

python modules/user-interaction-heatmap-visualization/live_heatmap_visualization.py --heatmap_yaml="heatmap_door.yaml" --evaluation_yaml="evaluation_door.yaml"

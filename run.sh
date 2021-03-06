


## tutorial from the repo
# visualize data from the code. can run
#python dense_correspondence/dataset/simple_datasets_test.py
#python dense_correspondence/training/training_tutorial.py
#python dense_correspondence/evaluation/evaluation_qualitative_tutorial.py
# visualization
#python modules/user-interaction-heatmap-visualization/live_heatmap_visualization.py




#python dense_correspondence/dataset/simple_datasets_test.py --data_name=open_door_1207_with_images.yaml
#python dense_correspondence/training/training_tutorial.py  --data_name=open_door_1207_with_images.yaml --run_prefix="open_door_1216" --training_yaml=training_door.yaml

#python modules/user-interaction-heatmap-visualization/live_heatmap_visualization.py --heatmap_yaml="heatmap_door.yaml" --evaluation_yaml="evaluation_door.yaml"




#== add eval
#python dense_correspondence/training/training_tutorial.py  --data_name=open_door_1207_with_images512.yaml --run_prefix="open_door_images512_1220_eval" --training_yaml=training_door.yaml
# == smaller learning rate
#python dense_correspondence/training/training_tutorial.py  --data_name=open_door_1207_with_images512.yaml --run_prefix="open_door_images512_1220_eval_5e5" --training_yaml=training_door.yaml


python dense_correspondence/training/training_tutorial.py  --data_name=open_door_1207_with_images512.yaml --run_prefix="open_door_images512_1220_eval_1e5" --training_yaml=training_door.yaml

#python modules/user-interaction-heatmap-visualization/live_heatmap_visualization.py --heatmap_yaml="heatmap_door.yaml" --evaluation_yaml="evaluation_door.yaml"









#python dense_correspondence/dataset/simple_datasets_test.py --data_name=pushtoalign_1202_with_images.yaml
#python dense_correspondence/training/training_tutorial.py  --data_name=pushtoalign_1202_with_images.yaml --run_prefix="pushtoalign_1220_350k_matrix" --training_yaml=training_pushtoalign.yaml
#python dense_correspondence/training/training_tutorial.py  --data_name=pushtoalign_1202_with_images.yaml --run_prefix="pushtoalign_1220_350k_matrix_decay1000" --training_yaml=training_pushtoalign.yaml

#python modules/user-interaction-heatmap-visualization/live_heatmap_visualization.py --heatmap_yaml="heatmap_pushtoalign.yaml" --evaluation_yaml="evaluation_pushtoalign.yaml"


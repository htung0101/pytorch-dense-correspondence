# Basic I/O utils
import yaml
import numpy as np
import os
import sys

def getDictFromYamlFilename(filename):
    """
    Read data from a YAML files
    """
    stream = file(filename)
    return yaml.load(stream)

def saveToYaml(data, filename):
    """
    Save a data to a YAML file
    """
    with open(filename, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)

def getDenseCorrespondenceSourceDir():
    return os.getenv("DC_SOURCE_DIR")


def dictFromPosQuat(pos, quat):
    """
    Make a dictionary from position and quaternion vectors
    """
    d = dict()
    d['translation'] = dict()
    d['translation']['x'] = pos[0]
    d['translation']['y'] = pos[1]
    d['translation']['z'] = pos[2]

    d['quaternion'] = dict()
    d['quaternion']['w'] = quat[0]
    d['quaternion']['x'] = quat[1]
    d['quaternion']['y'] = quat[2]
    d['quaternion']['z'] = quat[3]

    return d


def getQuaternionFromDict(d):
    """
    Get the quaternion from a dict describing a transform. The dict entry could be
    one of orientation, rotation, quaternion depending on the convention
    """
    quat = None
    quatNames = ['orientation', 'rotation', 'quaternion']
    for name in quatNames:
        if name in d:
            quat = d[name]


    if quat is None:
        raise ValueError("Error when trying to extract quaternion from dict, your dict doesn't contain a key in ['orientation', 'rotation', 'quaternion']")

    return quat

def getPaddedString(idx, width=6):
    return str(idx).zfill(width)

def set_cuda_visible_devices(gpu_list):
    """
    Sets CUDA_VISIBLE_DEVICES environment variable to only show certain gpus
    If gpu_list is empty does nothing
    :param gpu_list: list of gpus to set as visible
    :return: None
    """

    if len(gpu_list) == 0:
        return

    cuda_visible_devices = ""
    for gpu in gpu_list:
        cuda_visible_devices += str(gpu) + ","

    print "setting CUDA_VISIBLE_DEVICES = ", cuda_visible_devices
    os.environ["CUDA_VISIBLE_DEVICES"] = cuda_visible_devices

def get_defaults_config():
    dc_source_dir = getDenseCorrespondenceSourceDir()
    default_config_file = os.path.join(dc_source_dir, 'config', 'defaults.yaml')

    return getDictFromYamlFilename(default_config_file)


def add_dense_correspondence_to_python_path():
    dc_source_dir = getDenseCorrespondenceSourceDir()
    sys.path.append(dc_source_dir)

def convert_to_absolute_path(path):
    """
    Converts a potentially relative path to an absolute path by pre-pending the home directory
    :param path: absolute or relative path
    :type path: str
    :return: absolute path
    :rtype: str
    """

    if os.path.isdir(path):
        return path


    home_dir = os.path.expanduser("~")
    return os.path.join(home_dir, path)

class CameraIntrinsics(object):
    """
    Useful class for wrapping camera intrinsics and loading them from a
    camera_info.yaml file
    """
    def __init__(self, cx, cy, fx, fy, width, height):
        self.cx = cx
        self.cy = cy
        self.fx = fx
        self.fy = fy
        self.width = width
        self.height = height

    @staticmethod
    def from_yaml_file(filename):
        config = getDictFromYamlFilename(filename)

        fx = config['camera_matrix']['data'][0]
        cx = config['camera_matrix']['data'][2]

        fy = config['camera_matrix']['data'][4]
        cy = config['camera_matrix']['data'][5]

        width = config['image_width']
        height = config['image_height']

        return CameraIntrinsics(cx, cy, fx, fy, width, height)

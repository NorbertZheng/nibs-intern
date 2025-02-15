##################################
# Created on 19:46, Nov. 5th, 2020
# Author: fassial
# Filename: UNet.py
##################################
# dep
import os
import skimage.io as io
import skimage.transform as trans
# local dep
from model import *

# macro
EXPR_PATH = os.path.join(".", "img")
EXPR_CURR = "mouse"
MODEL_HDF5 = "unet-%s.hdf5"

# def UNet class
class UNet:
    def __init__(self, model_path = (MODEL_HDF5%EXPR_CURR)):
        # init model
        self.model = unet()
        # load model_hdf5
        self.model.load_weights(model_path)

    def predict(self, X, verbose=0, target_size=(256,256)):
        # record origin_size
        origin_size = X.shape
        # scale & resize X
        X = X / 255
        X = trans.resize(X, target_size)
        X = np.reshape(X, (1,)+X.shape+(1,))
        # get predict result
        y = self.model.predict(X,
            verbose = verbose
        )[0,:,:,0]
        y = trans.resize(y, origin_size)
        return y

if __name__ == "__main__":
    # inst Unet
    UNet_inst = UNet(model_path = (MODEL_HDF5%EXPR_CURR))
    # read gray(bit-width 8, shape(x,x))
    img_gray = io.imread(os.path.join(EXPR_PATH, "gray.png"), as_grey = True)
    # predict
    img_pred = UNet_inst.predict(X = img_gray, verbose = 1); print(img_pred.shape)
    # write pred
    io.imsave(os.path.join(EXPR_PATH, "predict.png"), img_pred)


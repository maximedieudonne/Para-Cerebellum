
# input : 
# original image
# mask segmentation you want to overlay
# your personal lut
# output : image and mask overlay

import numpy as np
import nibabel as nib
import cv2
import pandas as pd


def get_slices(img_path, slices, mask_path, lut_path):
    # load
    img = nib.load(img_path)
    mask = nib.load(mask_path)
    data_img = img.get_data()
    data_mask = mask.get_data()
    nb_slice = len(slices)
    list_slices = [0] * nb_slice
    idx_list_slices = 0
    for num_slice in slices:
        # add function that find slice we need
        data_imgslice = data_img[num_slice, :, :]
        data_maskslice = data_mask[num_slice, :, :]

        # Data are normalized because cv2 maps {0,1} to {0,255}
        # e.g any value greater than 1 is equal to 255
        data_norm_imgslice = (data_imgslice - np.min(data_imgslice)) / (np.max(data_imgslice) - np.min(data_imgslice))
        data_norm_imgslice = np.concatenate(
            (data_norm_imgslice[:, :, None], data_norm_imgslice[:, :, None], data_norm_imgslice[:, :, None]), 2)

        # build lut
        lut = pd.read_csv(lut_path)
        RGB = pd.DataFrame.to_numpy(lut[['Red', 'Green', 'Blue']])

        # apply lut
        data_maskslice_R = np.zeros(data_maskslice.shape)
        data_maskslice_G = np.zeros(data_maskslice.shape)
        data_maskslice_B = np.zeros(data_maskslice.shape)

        for label in range(1, 35):
            data_maskslice_R[data_maskslice == label] = RGB[label - 1, 0]
            data_maskslice_G[data_maskslice == label] = RGB[label - 1, 1]
            data_maskslice_B[data_maskslice == label] = RGB[label - 1, 2]

        data_maskslice_RGB = np.concatenate(
            (data_maskslice_R[:, :, None], data_maskslice_G[:, :, None], data_maskslice_B[:, :, None]), 2)
        data_norm_maskslice_RGB = (data_maskslice_RGB - np.min(data_maskslice_RGB)) / (
                np.max(data_maskslice_RGB) - np.min(data_maskslice_RGB))

        # overlay
        alpha = 0.5
        beta = 1 - alpha
        img_overlay = cv2.addWeighted(data_norm_imgslice, alpha, data_norm_maskslice_RGB, beta, 0.0)
        img_overlay = np.rot90(img_overlay)

        # stock in list_slices
        list_slices[idx_list_slices] = img_overlay
        idx_list_slices = idx_list_slices + 1

        # display
        cv2.imshow("seg", img_overlay)
        cv2.waitKey(0)

    return list_slices


import cv2
import os

def rotate_flip_img(main_img_loc, file_name, save_loc):
    print(main_img_loc,'/',file_name, '///', save_loc)
    inputimg = cv2.imread(main_img_loc+'/'+file_name)

    img_r90 = cv2.rotate(inputimg, cv2.ROTATE_90_CLOCKWISE)
    img_r180 = cv2.rotate(inputimg, cv2.ROTATE_180)
    img_r270 = cv2.rotate(inputimg, cv2.ROTATE_90_COUNTERCLOCKWISE)

    inputimg_filp_0 = cv2.flip(inputimg,0)
    inputimg_filp_1 = cv2.flip(inputimg,1)
    inputimg_ro90_flip_0 = cv2.flip(img_r90,0)
    inputimg_ro90_flip_1 = cv2.flip(img_r90,1)

    file_name_split = file_name.split('.')
    print(file_name_split[0])

    cv2.imwrite(save_loc+'/'+file_name, inputimg)
    cv2.imwrite(save_loc+'/'+file_name_split[0]+'_r90.'+file_name_split[1], img_r90)
    cv2.imwrite(save_loc+'/'+file_name_split[0]+'_r180.'+file_name_split[1], img_r180)
    cv2.imwrite(save_loc+'/'+file_name_split[0]+'_r270.'+file_name_split[1], img_r270)

    cv2.imwrite(save_loc+'/'+file_name_split[0]+'_flip0.'+file_name_split[1], inputimg_filp_0)
    cv2.imwrite(save_loc+'/'+file_name_split[0]+'_flip1.'+file_name_split[1], inputimg_filp_1)
    cv2.imwrite(save_loc+'/'+file_name_split[0]+'_r90_flip0.'+file_name_split[1], inputimg_ro90_flip_0)
    cv2.imwrite(save_loc+'/'+file_name_split[0]+'_r90_flip1.'+file_name_split[1], inputimg_ro90_flip_1)


def data_loc(make_data_loc, save_loc):
    data_list = os.listdir(make_data_loc)

    for i in data_list:
        rotate_flip_img(make_data_loc, i, save_loc)

    # for ii in mask_list:
    #     print(ii)
    #     rotate_flip_img(mask_list, i, save_loc)

main_img = 'TrainTest_Prepro/lim4/test/mask'
# main_img = 'Train_img/img_crop_resize/MALIGNANT_mask'

save_loc = 'TrainTest_Prepro/lim4Ag/test/mask'
# save_loc = 'Train_img/img_crop_resize_Aug/MALIGNANT_mask'


data_loc(main_img, save_loc)

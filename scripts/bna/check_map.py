import nibabel as nib
from nilearn import plotting

# 載入 activation NIfTI 檔案
activation_img = nib.load("output/capsnet/sub-14_conv3_resampled_to_bna.nii.gz")

# 顯示 activation map
display = plotting.plot_stat_map(
    activation_img,
    display_mode="ortho",
    threshold=0.1,
    title="Activation Map (sub-14 conv3)"
)
display.savefig("figures/bna/activation_map.png")

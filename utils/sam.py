from sam2_module.sam2.sam2_image_predictor import SAM2ImagePredictor
from sam2_module.sam2.build_sam import build_sam2

sam2_checkpoint = "model/sam2.1_hiera_tiny.pt"
model_cfg = "configs/sam2.1/sam2.1_hiera_t.yaml"

sam2_model = build_sam2(model_cfg, sam2_checkpoint, device="mps")

predictor = SAM2ImagePredictor(sam2_model)

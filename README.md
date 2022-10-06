# PixelMend

A self-hosted, browser-based image inpainting tool that erases unwanted objects, repairs old photos and extends images using state-of-the-art AI models.

## What This Project Does

Removing a watermark, a stranger in the background or a scratch on an old photo usually
means hours in a photo editor. PixelMend fills in a masked area of an image with an AI
model, all on your own machine (CPU, NVIDIA GPU or Apple Silicon).

Features so far:

- **Object removal** with fast, dedicated inpainting models: LaMa, Anime-LaMa, MAT, FcF,
  ZITS, MI-GAN, Manga, LDM and OpenCV.
- **Prompt-guided editing** with Stable Diffusion 1.5/2, SDXL, Kandinsky 2.2,
  Paint by Example, InstructPix2Pix, BrushNet, PowerPaint (v1/v2), ControlNet and AnyText
  (text rendering).
- **High-resolution strategies**: process large images at original size, resized, or
  cropped around the mask.
- **Plugins**: interactive segmentation (Segment Anything / SAM 2 / MobileSAM), background
  removal (RMBG / rembg), anime segmentation, Real-ESRGAN upscaling and GFPGAN /
  RestoreFormer face restoration.
- **REST API** (FastAPI + Socket.IO) for inpainting, model switching and plugins.
- **Batch processing** from the command line for whole folders of images and masks.
- **Web config page** (Gradio) for building a server configuration file without editing JSON.

## How to Run This Project

1. Install Python 3.10, then clone and install:

   ```bash
   git clone https://github.com/hadeeddev921/pixelmend.git
   cd pixelmend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   pip install -e .
   ```

2. Start the API server:

   ```bash
   pixelmend start --model lama --device cpu --port 8080
   ```

3. Or batch-process a folder:

   ```bash
   pixelmend run --model lama --device cpu --image ./images --mask ./masks --output ./output
   ```

The browser editor is under development.

## License

Licensed under the Apache License 2.0. See [LICENSE](LICENSE).

# PixelMend

A self-hosted, browser-based image inpainting tool that erases unwanted objects, repairs old photos and extends images using state-of-the-art AI models.

## What This Project Does

Removing a watermark, a stranger in the background or a scratch on an old photo usually
means hours in a photo editor. PixelMend fills in a masked area of an image with an AI
model, all on your own machine (CPU, NVIDIA GPU or Apple Silicon).

Features so far:

- **Object removal** with fast, dedicated inpainting models: LaMa, Anime-LaMa, MAT, FcF,
  ZITS, MI-GAN, Manga, LDM and OpenCV.
- **High-resolution strategies**: process large images at original size, resized, or
  cropped around the mask.

## Status

Early development. The model backend is being built first; the web editor will follow.

## License

Licensed under the Apache License 2.0. See [LICENSE](LICENSE).

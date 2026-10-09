# HeteroMesh profile illustration

`cluster-refined.gif` depicts a conceptual four-device setup, with macOS as an example coordinator. Sequential transfers pass through the coordinator; this is an architecture illustration, not a recording of validated multi-device H3 inference.

Device glyphs use the unmodified geometry of [Lucide](https://github.com/lucide-icons/lucide) `laptop`, `monitor`, and `smartphone` icons. Original SVG sources are included here. Color and stroke width are adapted for the animation. See [LICENSE](LICENSE) for ISC and Feather MIT notices.

## Model-sharding film

`model-sharding.gif` is the current profile illustration: a 8-second, 1120 × 630 concept animation showing a Transformer model split into four schematic weight shards, resident weights on heterogeneous devices, and intermediate activation relay. The four groups are illustrative, not a measured allocation. Windows CUDA and iOS compute are target paths; the film is not a recording of validated four-device inference. Hardware and model geometry are drawn specifically for this film.

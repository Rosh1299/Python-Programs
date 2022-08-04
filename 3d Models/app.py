from platform import node
from pygltflib import GLTF2, Scene
from pygltflib.utils import ImageFormat

# gltf = GLTF2()

# scene = Scene()
# gltf.scenes.append(scene)

filename = "scene.gltf"
gltf = GLTF2().load(filename)
# gltf.convert_images(ImageFormat.FILE)
# img = gltf.images[1].uri
# print(img)
current_scene = gltf.scenes[gltf.scene]
node_index = current_scene.nodes[0]
box = gltf.nodes[node_index]
# print(gltf.images)
for index, i in enumerate(gltf.images):
    print(index, i.uri)

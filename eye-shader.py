import bpy, mathutils

mat = bpy.data.materials.new(name = "Eyes")
mat.use_nodes = True
#initialize NodeGroup node group
def nodegroup_node_group():

    nodegroup = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "NodeGroup")

    nodegroup.color_tag = 'NONE'
    nodegroup.description = ""
    nodegroup.default_group_node_width = 140
    

    #nodegroup interface
    #Socket Value
    value_socket = nodegroup.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    value_socket.default_value = 0.0
    value_socket.min_value = -3.4028234663852886e+38
    value_socket.max_value = 3.4028234663852886e+38
    value_socket.subtype = 'NONE'
    value_socket.attribute_domain = 'POINT'

    #Socket Value
    value_socket_1 = nodegroup.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    value_socket_1.default_value = 0.0
    value_socket_1.min_value = -3.4028234663852886e+38
    value_socket_1.max_value = 3.4028234663852886e+38
    value_socket_1.subtype = 'NONE'
    value_socket_1.attribute_domain = 'POINT'

    #Socket Vector
    vector_socket = nodegroup.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
    vector_socket.default_value = (0.0, 0.0, 0.0)
    vector_socket.min_value = -10000.0
    vector_socket.max_value = 10000.0
    vector_socket.subtype = 'NONE'
    vector_socket.attribute_domain = 'POINT'

    #Socket Vector
    vector_socket_1 = nodegroup.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
    vector_socket_1.default_value = (-0.20000000298023224, 0.0, 0.0)
    vector_socket_1.min_value = -10000.0
    vector_socket_1.max_value = 10000.0
    vector_socket_1.subtype = 'NONE'
    vector_socket_1.attribute_domain = 'POINT'

    #Socket Flatness
    flatness_socket = nodegroup.interface.new_socket(name = "Flatness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    flatness_socket.default_value = 8.0
    flatness_socket.min_value = 0.0
    flatness_socket.max_value = 10000.0
    flatness_socket.subtype = 'NONE'
    flatness_socket.attribute_domain = 'POINT'

    #Socket Size
    size_socket = nodegroup.interface.new_socket(name = "Size", in_out='INPUT', socket_type = 'NodeSocketFloat')
    size_socket.default_value = 0.10000000149011612
    size_socket.min_value = -3.4028234663852886e+38
    size_socket.max_value = 3.4028234663852886e+38
    size_socket.subtype = 'NONE'
    size_socket.attribute_domain = 'POINT'

    #Socket Angle
    angle_socket = nodegroup.interface.new_socket(name = "Angle", in_out='INPUT', socket_type = 'NodeSocketFloat')
    angle_socket.default_value = 0.0
    angle_socket.min_value = -3.4028234663852886e+38
    angle_socket.max_value = 3.4028234663852886e+38
    angle_socket.subtype = 'ANGLE'
    angle_socket.attribute_domain = 'POINT'

    #Socket Height
    height_socket = nodegroup.interface.new_socket(name = "Height", in_out='INPUT', socket_type = 'NodeSocketFloat')
    height_socket.default_value = 0.0
    height_socket.min_value = -10000.0
    height_socket.max_value = 10000.0
    height_socket.subtype = 'NONE'
    height_socket.attribute_domain = 'POINT'

    #Socket Vector
    vector_socket_2 = nodegroup.interface.new_socket(name = "Vector", in_out='INPUT', socket_type = 'NodeSocketVector')
    vector_socket_2.default_value = (0.0, 0.0, 0.0)
    vector_socket_2.min_value = -10000.0
    vector_socket_2.max_value = 10000.0
    vector_socket_2.subtype = 'NONE'
    vector_socket_2.attribute_domain = 'POINT'


    #initialize nodegroup nodes
    #node Separate XYZ
    separate_xyz = nodegroup.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"

    #node Vector Math.013
    vector_math_013 = nodegroup.nodes.new("ShaderNodeVectorMath")
    vector_math_013.name = "Vector Math.013"
    vector_math_013.operation = 'DISTANCE'

    #node Math
    math = nodegroup.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'ADD'
    math.use_clamp = False
    #Value_001
    math.inputs[1].default_value = 0.10000000149011612

    #node Combine XYZ
    combine_xyz = nodegroup.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    #X
    combine_xyz.inputs[0].default_value = 0.0
    #Z
    combine_xyz.inputs[2].default_value = 0.0

    #node Math.006
    math_006 = nodegroup.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = 'GREATER_THAN'
    math_006.use_clamp = False

    #node Math.005
    math_005 = nodegroup.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = 'SUBTRACT'
    math_005.use_clamp = False
    #Value_001
    math_005.inputs[1].default_value = -0.019999999552965164

    #node Math.008
    math_008 = nodegroup.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.operation = 'MULTIPLY'
    math_008.use_clamp = False

    #node Vector Math.021
    vector_math_021 = nodegroup.nodes.new("ShaderNodeVectorMath")
    vector_math_021.name = "Vector Math.021"
    vector_math_021.operation = 'ADD'
    #Vector
    vector_math_021.inputs[0].default_value = (0.0, 0.0, 0.0)
    #Vector_001
    vector_math_021.inputs[1].default_value = (0.0, 0.0, 0.0)

    #node Math.009
    math_009 = nodegroup.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.operation = 'LESS_THAN'
    math_009.use_clamp = False

    #node Math.007
    math_007 = nodegroup.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.operation = 'LESS_THAN'
    math_007.use_clamp = False

    #node Math.001
    math_001 = nodegroup.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = False

    #node Math.002
    math_002 = nodegroup.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'ADD'
    math_002.use_clamp = False

    #node Math.003
    math_003 = nodegroup.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'LESS_THAN'
    math_003.use_clamp = False
    #Value_001
    math_003.inputs[1].default_value = 1.0

    #node Math.010
    math_010 = nodegroup.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.operation = 'MULTIPLY'
    math_010.use_clamp = False

    #node Group Output
    group_output = nodegroup.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Value.001
    value_001 = nodegroup.nodes.new("ShaderNodeValue")
    value_001.name = "Value.001"

    value_001.outputs[0].default_value = 9.799999237060547
    #node Group Input.001
    group_input_001 = nodegroup.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"

    #node Value
    value = nodegroup.nodes.new("ShaderNodeValue")
    value.name = "Value"

    value.outputs[0].default_value = 0.10000002384185791
    #node Texture Coordinate.003
    texture_coordinate_003 = nodegroup.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_003.name = "Texture Coordinate.003"
    texture_coordinate_003.from_instancer = False

    #node Vector Math.016
    vector_math_016 = nodegroup.nodes.new("ShaderNodeVectorMath")
    vector_math_016.name = "Vector Math.016"
    vector_math_016.operation = 'SUBTRACT'

    #node Vector Math.018
    vector_math_018 = nodegroup.nodes.new("ShaderNodeVectorMath")
    vector_math_018.name = "Vector Math.018"
    vector_math_018.operation = 'ADD'

    #node Group Input.002
    group_input_002 = nodegroup.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"

    #node Separate XYZ.002
    separate_xyz_002 = nodegroup.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_002.name = "Separate XYZ.002"

    #node Vector Math.017
    vector_math_017 = nodegroup.nodes.new("ShaderNodeVectorMath")
    vector_math_017.name = "Vector Math.017"
    vector_math_017.operation = 'SUBTRACT'
    #Vector_001
    vector_math_017.inputs[1].default_value = (0.5, 0.5, 0.0)

    #node Vector Math.014
    vector_math_014 = nodegroup.nodes.new("ShaderNodeVectorMath")
    vector_math_014.name = "Vector Math.014"
    vector_math_014.operation = 'MULTIPLY'
    #Vector_001
    vector_math_014.inputs[1].default_value = (1.0, 0.5, 1.0)

    #node Vector Rotate
    vector_rotate = nodegroup.nodes.new("ShaderNodeVectorRotate")
    vector_rotate.name = "Vector Rotate"
    vector_rotate.invert = False
    vector_rotate.rotation_type = 'Z_AXIS'
    #Center
    vector_rotate.inputs[1].default_value = (0.0, -0.09999999403953552, 0.0)

    #node Vector Math
    vector_math = nodegroup.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'MULTIPLY'
    #Vector
    vector_math.inputs[0].default_value = (0.0, -1.0, 0.0)

    #node Vector Math.015
    vector_math_015 = nodegroup.nodes.new("ShaderNodeVectorMath")
    vector_math_015.name = "Vector Math.015"
    vector_math_015.operation = 'DISTANCE'

    #node Vector Math.020
    vector_math_020 = nodegroup.nodes.new("ShaderNodeVectorMath")
    vector_math_020.name = "Vector Math.020"
    vector_math_020.operation = 'SUBTRACT'
    #Vector_001
    vector_math_020.inputs[1].default_value = (0.0, 0.0, 0.0)

    #node Vector Math.001
    vector_math_001 = nodegroup.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'ADD'

    #node Combine XYZ.001
    combine_xyz_001 = nodegroup.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    #X
    combine_xyz_001.inputs[0].default_value = 0.0
    #Z
    combine_xyz_001.inputs[2].default_value = 0.0

    #node Group Input.003
    group_input_003 = nodegroup.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"

    #node Group Input
    group_input = nodegroup.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    #node Group Input.004
    group_input_004 = nodegroup.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"


    #Set locations
    separate_xyz.location = (869.4960327148438, -408.1305236816406)
    vector_math_013.location = (615.5546875, -45.51359176635742)
    math.location = (500.13812255859375, 189.678955078125)
    combine_xyz.location = (258.853515625, 69.92045593261719)
    math_006.location = (1054.89208984375, 136.189697265625)
    math_005.location = (850.0811767578125, 36.686370849609375)
    math_008.location = (1355.849853515625, -154.8842010498047)
    vector_math_021.location = (-1536.47509765625, -211.31167602539062)
    math_009.location = (1303.8765869140625, -438.83685302734375)
    math_007.location = (1028.2794189453125, -135.6172332763672)
    math_001.location = (1549.6376953125, -689.78955078125)
    math_002.location = (1850.0, -665.3162231445312)
    math_003.location = (2061.263671875, -706.8045043945312)
    math_010.location = (1823.7628173828125, -158.28187561035156)
    group_output.location = (2360.119384765625, -628.0878295898438)
    value_001.location = (213.4807891845703, 344.922119140625)
    group_input_001.location = (-169.23529052734375, 361.1872863769531)
    value.location = (-189.59774780273438, -794.012451171875)
    texture_coordinate_003.location = (-1311.9498291015625, 152.16424560546875)
    vector_math_016.location = (-548.9475708007812, -21.012229919433594)
    vector_math_018.location = (-1075.184326171875, -35.330265045166016)
    group_input_002.location = (-378.7327575683594, -668.818115234375)
    separate_xyz_002.location = (-655.127685546875, 270.29302978515625)
    vector_math_017.location = (-849.4864501953125, 19.562118530273438)
    vector_math_014.location = (-316.2935791015625, 7.361164093017578)
    vector_rotate.location = (-139.4859619140625, -47.18299865722656)
    vector_math.location = (135.12896728515625, -499.54937744140625)
    vector_math_015.location = (679.1390991210938, -390.7365417480469)
    vector_math_020.location = (440.72076416015625, -259.888671875)
    vector_math_001.location = (107.79427337646484, -149.8335723876953)
    combine_xyz_001.location = (-229.32003784179688, -353.7170715332031)
    group_input_003.location = (-486.74884033203125, -217.0140838623047)
    group_input.location = (-1356.2255859375, -404.74334716796875)
    group_input_004.location = (-1559.097412109375, 93.484619140625)

    #Set dimensions
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    vector_math_013.width, vector_math_013.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    math_008.width, math_008.height = 140.0, 100.0
    vector_math_021.width, vector_math_021.height = 140.0, 100.0
    math_009.width, math_009.height = 140.0, 100.0
    math_007.width, math_007.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    math_002.width, math_002.height = 138.9512939453125, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    math_010.width, math_010.height = 148.5933837890625, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    value_001.width, value_001.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    value.width, value.height = 140.0, 100.0
    texture_coordinate_003.width, texture_coordinate_003.height = 140.0, 100.0
    vector_math_016.width, vector_math_016.height = 140.0, 100.0
    vector_math_018.width, vector_math_018.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    separate_xyz_002.width, separate_xyz_002.height = 140.0, 100.0
    vector_math_017.width, vector_math_017.height = 140.0, 100.0
    vector_math_014.width, vector_math_014.height = 140.0, 100.0
    vector_rotate.width, vector_rotate.height = 140.0, 100.0
    vector_math.width, vector_math.height = 150.48770141601562, 100.0
    vector_math_015.width, vector_math_015.height = 140.0, 100.0
    vector_math_020.width, vector_math_020.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 130.29849243164062, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0

    #initialize nodegroup links
    #vector_math_018.Vector -> vector_math_017.Vector
    nodegroup.links.new(vector_math_018.outputs[0], vector_math_017.inputs[0])
    #vector_math_017.Vector -> vector_math_016.Vector
    nodegroup.links.new(vector_math_017.outputs[0], vector_math_016.inputs[0])
    #math_005.Value -> math_006.Value
    nodegroup.links.new(math_005.outputs[0], math_006.inputs[0])
    #vector_math_013.Value -> math_005.Value
    nodegroup.links.new(vector_math_013.outputs[1], math_005.inputs[0])
    #vector_math_013.Value -> math_007.Value
    nodegroup.links.new(vector_math_013.outputs[1], math_007.inputs[0])
    #math_006.Value -> math_008.Value
    nodegroup.links.new(math_006.outputs[0], math_008.inputs[0])
    #math_007.Value -> math_008.Value
    nodegroup.links.new(math_007.outputs[0], math_008.inputs[1])
    #vector_math_015.Value -> separate_xyz.Vector
    nodegroup.links.new(vector_math_015.outputs[1], separate_xyz.inputs[0])
    #math_009.Value -> math_010.Value
    nodegroup.links.new(math_009.outputs[0], math_010.inputs[1])
    #math_008.Value -> math_010.Value
    nodegroup.links.new(math_008.outputs[0], math_010.inputs[0])
    #vector_math_020.Vector -> vector_math_015.Vector
    nodegroup.links.new(vector_math_020.outputs[0], vector_math_015.inputs[0])
    #vector_math_015.Value -> math_009.Value
    nodegroup.links.new(vector_math_015.outputs[1], math_009.inputs[0])
    #vector_math.Vector -> vector_math_015.Vector
    nodegroup.links.new(vector_math.outputs[0], vector_math_015.inputs[1])
    #math.Value -> math_007.Value
    nodegroup.links.new(math.outputs[0], math_007.inputs[1])
    #combine_xyz.Vector -> vector_math_013.Vector
    nodegroup.links.new(combine_xyz.outputs[0], vector_math_013.inputs[1])
    #math.Value -> math_006.Value
    nodegroup.links.new(math.outputs[0], math_006.inputs[1])
    #group_input.Vector -> vector_math_018.Vector
    nodegroup.links.new(group_input.outputs[0], vector_math_018.inputs[1])
    #group_input.Vector -> vector_math_016.Vector
    nodegroup.links.new(group_input.outputs[1], vector_math_016.inputs[1])
    #math_009.Value -> math_001.Value
    nodegroup.links.new(math_009.outputs[0], math_001.inputs[1])
    #math_007.Value -> math_001.Value
    nodegroup.links.new(math_007.outputs[0], math_001.inputs[0])
    #math_001.Value -> math_002.Value
    nodegroup.links.new(math_001.outputs[0], math_002.inputs[0])
    #math_007.Value -> math_002.Value
    nodegroup.links.new(math_007.outputs[0], math_002.inputs[1])
    #math_002.Value -> math_003.Value
    nodegroup.links.new(math_002.outputs[0], math_003.inputs[0])
    #math_003.Value -> group_output.Value
    nodegroup.links.new(math_003.outputs[0], group_output.inputs[1])
    #math_010.Value -> group_output.Value
    nodegroup.links.new(math_010.outputs[0], group_output.inputs[0])
    #group_input_001.Flatness -> math.Value
    nodegroup.links.new(group_input_001.outputs[2], math.inputs[0])
    #group_input_001.Flatness -> combine_xyz.Y
    nodegroup.links.new(group_input_001.outputs[2], combine_xyz.inputs[1])
    #group_input_002.Size -> vector_math.Vector
    nodegroup.links.new(group_input_002.outputs[3], vector_math.inputs[1])
    #group_input_002.Size -> math_009.Value
    nodegroup.links.new(group_input_002.outputs[3], math_009.inputs[1])
    #vector_math_014.Vector -> vector_rotate.Vector
    nodegroup.links.new(vector_math_014.outputs[0], vector_rotate.inputs[0])
    #vector_math_016.Vector -> vector_math_014.Vector
    nodegroup.links.new(vector_math_016.outputs[0], vector_math_014.inputs[0])
    #group_input_003.Angle -> vector_rotate.Angle
    nodegroup.links.new(group_input_003.outputs[4], vector_rotate.inputs[3])
    #vector_rotate.Vector -> vector_math_001.Vector
    nodegroup.links.new(vector_rotate.outputs[0], vector_math_001.inputs[0])
    #vector_math_001.Vector -> vector_math_020.Vector
    nodegroup.links.new(vector_math_001.outputs[0], vector_math_020.inputs[0])
    #vector_math_001.Vector -> vector_math_013.Vector
    nodegroup.links.new(vector_math_001.outputs[0], vector_math_013.inputs[0])
    #combine_xyz_001.Vector -> vector_math_001.Vector
    nodegroup.links.new(combine_xyz_001.outputs[0], vector_math_001.inputs[1])
    #group_input_003.Height -> combine_xyz_001.Y
    nodegroup.links.new(group_input_003.outputs[5], combine_xyz_001.inputs[1])
    #group_input_004.Vector -> vector_math_018.Vector
    nodegroup.links.new(group_input_004.outputs[6], vector_math_018.inputs[0])
    #group_input_004.Vector -> separate_xyz_002.Vector
    nodegroup.links.new(group_input_004.outputs[6], separate_xyz_002.inputs[0])
    return nodegroup

nodegroup = nodegroup_node_group()

#initialize Eye node group
def eye_node_group():

    eye = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "Eye")

    eye.color_tag = 'NONE'
    eye.description = ""
    eye.default_group_node_width = 140
    

    #eye interface
    #Socket Value
    value_socket_2 = eye.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    value_socket_2.default_value = 0.0
    value_socket_2.min_value = 0.0
    value_socket_2.max_value = 1.0
    value_socket_2.subtype = 'NONE'
    value_socket_2.attribute_domain = 'POINT'

    #Socket X
    x_socket = eye.interface.new_socket(name = "X", in_out='INPUT', socket_type = 'NodeSocketFloat')
    x_socket.default_value = 2.0
    x_socket.min_value = -10000.0
    x_socket.max_value = 10000.0
    x_socket.subtype = 'NONE'
    x_socket.attribute_domain = 'POINT'

    #Socket Eye
    eye_socket = eye.interface.new_socket(name = "Eye", in_out='INPUT', socket_type = 'NodeSocketFloat')
    eye_socket.default_value = 0.0
    eye_socket.min_value = 0.0
    eye_socket.max_value = 1.0
    eye_socket.subtype = 'NONE'
    eye_socket.attribute_domain = 'POINT'

    #Socket Pupil Size
    pupil_size_socket = eye.interface.new_socket(name = "Pupil Size", in_out='INPUT', socket_type = 'NodeSocketFloat')
    pupil_size_socket.default_value = 0.5
    pupil_size_socket.min_value = 0.0
    pupil_size_socket.max_value = 1.0
    pupil_size_socket.subtype = 'NONE'
    pupil_size_socket.attribute_domain = 'POINT'

    #Socket Eye Offset
    eye_offset_socket = eye.interface.new_socket(name = "Eye Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
    eye_offset_socket.default_value = (0.0, 0.0, 0.0)
    eye_offset_socket.min_value = -10000.0
    eye_offset_socket.max_value = 10000.0
    eye_offset_socket.subtype = 'NONE'
    eye_offset_socket.attribute_domain = 'POINT'

    #Socket Pupil Offset
    pupil_offset_socket = eye.interface.new_socket(name = "Pupil Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
    pupil_offset_socket.default_value = (0.0, 0.0, 0.0)
    pupil_offset_socket.min_value = -10000.0
    pupil_offset_socket.max_value = 10000.0
    pupil_offset_socket.subtype = 'NONE'
    pupil_offset_socket.attribute_domain = 'POINT'

    #Socket Eyebrow Flatness
    eyebrow_flatness_socket = eye.interface.new_socket(name = "Eyebrow Flatness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    eyebrow_flatness_socket.default_value = 0.20000052452087402
    eyebrow_flatness_socket.min_value = 0.0
    eyebrow_flatness_socket.max_value = 10000.0
    eyebrow_flatness_socket.subtype = 'NONE'
    eyebrow_flatness_socket.attribute_domain = 'POINT'

    #Socket EyeBrow Size
    eyebrow_size_socket = eye.interface.new_socket(name = "EyeBrow Size", in_out='INPUT', socket_type = 'NodeSocketFloat')
    eyebrow_size_socket.default_value = 0.09999999403953552
    eyebrow_size_socket.min_value = -3.4028234663852886e+38
    eyebrow_size_socket.max_value = 3.4028234663852886e+38
    eyebrow_size_socket.subtype = 'NONE'
    eyebrow_size_socket.attribute_domain = 'POINT'

    #Socket Eyebrow angle
    eyebrow_angle_socket = eye.interface.new_socket(name = "Eyebrow angle", in_out='INPUT', socket_type = 'NodeSocketFloat')
    eyebrow_angle_socket.default_value = 0.0
    eyebrow_angle_socket.min_value = -3.4028234663852886e+38
    eyebrow_angle_socket.max_value = 3.4028234663852886e+38
    eyebrow_angle_socket.subtype = 'ANGLE'
    eyebrow_angle_socket.attribute_domain = 'POINT'

    #Socket EyeBrow height
    eyebrow_height_socket = eye.interface.new_socket(name = "EyeBrow height", in_out='INPUT', socket_type = 'NodeSocketFloat')
    eyebrow_height_socket.default_value = -0.10000000149011612
    eyebrow_height_socket.min_value = -10000.0
    eyebrow_height_socket.max_value = 10000.0
    eyebrow_height_socket.subtype = 'NONE'
    eyebrow_height_socket.attribute_domain = 'POINT'

    #Socket UV
    uv_socket = eye.interface.new_socket(name = "UV", in_out='INPUT', socket_type = 'NodeSocketVector')
    uv_socket.default_value = (0.0, 0.0, 0.0)
    uv_socket.min_value = -10000.0
    uv_socket.max_value = 10000.0
    uv_socket.subtype = 'NONE'
    uv_socket.attribute_domain = 'POINT'


    #initialize eye nodes
    #node Math.001
    math_001_1 = eye.nodes.new("ShaderNodeMath")
    math_001_1.name = "Math.001"
    math_001_1.operation = 'MULTIPLY'
    math_001_1.use_clamp = False

    #node Map Range
    map_range = eye.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.clamp = True
    map_range.data_type = 'FLOAT'
    map_range.interpolation_type = 'LINEAR'
    #From Min
    map_range.inputs[1].default_value = 0.0
    #From Max
    map_range.inputs[2].default_value = 1.0
    #To Min
    map_range.inputs[3].default_value = -1.0
    #To Max
    map_range.inputs[4].default_value = 1.0

    #node Separate XYZ
    separate_xyz_1 = eye.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_1.name = "Separate XYZ"

    #node Vector Math.002
    vector_math_002 = eye.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = 'MULTIPLY'
    #Vector_001
    vector_math_002.inputs[1].default_value = (1.2000000476837158, 0.5, 1.0)

    #node Vector Math.001
    vector_math_001_1 = eye.nodes.new("ShaderNodeVectorMath")
    vector_math_001_1.name = "Vector Math.001"
    vector_math_001_1.operation = 'DISTANCE'
    #Vector_001
    vector_math_001_1.inputs[1].default_value = (0.0, 0.0, 0.0)

    #node Math
    math_1 = eye.nodes.new("ShaderNodeMath")
    math_1.name = "Math"
    math_1.operation = 'LESS_THAN'
    math_1.use_clamp = False
    #Value_001
    math_1.inputs[1].default_value = 0.10000002384185791

    #node Texture Coordinate.001
    texture_coordinate_001 = eye.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_001.name = "Texture Coordinate.001"
    texture_coordinate_001.from_instancer = False

    #node Vector Math.004
    vector_math_004 = eye.nodes.new("ShaderNodeVectorMath")
    vector_math_004.name = "Vector Math.004"
    vector_math_004.operation = 'SUBTRACT'
    #Vector_001
    vector_math_004.inputs[1].default_value = (0.5, 0.5499999523162842, 0.0)

    #node Vector Math.005
    vector_math_005 = eye.nodes.new("ShaderNodeVectorMath")
    vector_math_005.name = "Vector Math.005"
    vector_math_005.operation = 'SUBTRACT'

    #node Vector Math.003
    vector_math_003 = eye.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.operation = 'SUBTRACT'
    #Vector_001
    vector_math_003.inputs[1].default_value = (0.30000001192092896, 0.6499999761581421, 0.0)

    #node Combine XYZ
    combine_xyz_1 = eye.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_1.name = "Combine XYZ"
    #Y
    combine_xyz_1.inputs[1].default_value = 0.0
    #Z
    combine_xyz_1.inputs[2].default_value = 0.0

    #node Vector Math.011
    vector_math_011 = eye.nodes.new("ShaderNodeVectorMath")
    vector_math_011.name = "Vector Math.011"
    vector_math_011.operation = 'ADD'

    #node Group Input
    group_input_1 = eye.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"
    group_input_1.outputs[5].hide = True

    #node Separate XYZ.001
    separate_xyz_001 = eye.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"

    #node Vector Math.007
    vector_math_007 = eye.nodes.new("ShaderNodeVectorMath")
    vector_math_007.name = "Vector Math.007"
    vector_math_007.operation = 'DISTANCE'
    #Vector_001
    vector_math_007.inputs[1].default_value = (0.0, 0.0, 0.0)

    #node Texture Coordinate.002
    texture_coordinate_002 = eye.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_002.name = "Texture Coordinate.002"
    texture_coordinate_002.from_instancer = False

    #node Vector Math.006
    vector_math_006 = eye.nodes.new("ShaderNodeVectorMath")
    vector_math_006.name = "Vector Math.006"
    vector_math_006.operation = 'MULTIPLY'
    #Vector_001
    vector_math_006.inputs[1].default_value = (1.2000000476837158, 0.5, 1.0)

    #node Vector Math
    vector_math_1 = eye.nodes.new("ShaderNodeVectorMath")
    vector_math_1.name = "Vector Math"
    vector_math_1.operation = 'SCALE'
    #Scale
    vector_math_1.inputs[3].default_value = 1.0

    #node Vector Math.009
    vector_math_009 = eye.nodes.new("ShaderNodeVectorMath")
    vector_math_009.name = "Vector Math.009"
    vector_math_009.operation = 'SUBTRACT'

    #node Math.004
    math_004 = eye.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'DIVIDE'
    math_004.use_clamp = False

    #node Group Input.001
    group_input_001_1 = eye.nodes.new("NodeGroupInput")
    group_input_001_1.name = "Group Input.001"
    group_input_001_1.outputs[5].hide = True

    #node Math.002
    math_002_1 = eye.nodes.new("ShaderNodeMath")
    math_002_1.name = "Math.002"
    math_002_1.operation = 'GREATER_THAN'
    math_002_1.use_clamp = False
    #Value_001
    math_002_1.inputs[1].default_value = 0.10000000149011612

    #node Vector Math.008
    vector_math_008 = eye.nodes.new("ShaderNodeVectorMath")
    vector_math_008.name = "Vector Math.008"
    vector_math_008.operation = 'SUBTRACT'
    #Vector_001
    vector_math_008.inputs[1].default_value = (0.5, 0.5499999523162842, 0.0)

    #node Vector Math.012
    vector_math_012 = eye.nodes.new("ShaderNodeVectorMath")
    vector_math_012.name = "Vector Math.012"
    vector_math_012.operation = 'ADD'

    #node Vector Math.010
    vector_math_010 = eye.nodes.new("ShaderNodeVectorMath")
    vector_math_010.name = "Vector Math.010"
    vector_math_010.operation = 'ADD'

    #node Vector Math.013
    vector_math_013_1 = eye.nodes.new("ShaderNodeVectorMath")
    vector_math_013_1.name = "Vector Math.013"
    vector_math_013_1.operation = 'ADD'
    #Vector_001
    vector_math_013_1.inputs[1].default_value = (0.0, 0.0, 0.0)

    #node Vector Math.014
    vector_math_014_1 = eye.nodes.new("ShaderNodeVectorMath")
    vector_math_014_1.name = "Vector Math.014"
    vector_math_014_1.operation = 'ADD'
    #Vector
    vector_math_014_1.inputs[0].default_value = (0.0, -0.20000019669532776, 0.0)

    #node Group Input.003
    group_input_003_1 = eye.nodes.new("NodeGroupInput")
    group_input_003_1.name = "Group Input.003"
    group_input_003_1.outputs[5].hide = True

    #node Math.003
    math_003_1 = eye.nodes.new("ShaderNodeMath")
    math_003_1.name = "Math.003"
    math_003_1.operation = 'MULTIPLY'
    math_003_1.use_clamp = False

    #node Group Output
    group_output_1 = eye.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    #node Math.005
    math_005_1 = eye.nodes.new("ShaderNodeMath")
    math_005_1.name = "Math.005"
    math_005_1.operation = 'MULTIPLY'
    math_005_1.use_clamp = False

    #node Math.006
    math_006_1 = eye.nodes.new("ShaderNodeMath")
    math_006_1.name = "Math.006"
    math_006_1.operation = 'ADD'
    math_006_1.use_clamp = False

    #node Group Input.005
    group_input_005 = eye.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"

    #node Group Input.004
    group_input_004_1 = eye.nodes.new("NodeGroupInput")
    group_input_004_1.name = "Group Input.004"
    group_input_004_1.outputs[5].hide = True

    #node UV Map
    uv_map = eye.nodes.new("ShaderNodeUVMap")
    uv_map.name = "UV Map"
    uv_map.from_instancer = False
    uv_map.uv_map = ""

    #node Group
    group = eye.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = nodegroup

    #node Group Input.002
    group_input_002_1 = eye.nodes.new("NodeGroupInput")
    group_input_002_1.name = "Group Input.002"
    group_input_002_1.outputs[5].hide = True


    #Set locations
    math_001_1.location = (-923.3587036132812, -453.99713134765625)
    map_range.location = (-1156.2513427734375, -629.6893920898438)
    separate_xyz_1.location = (85.32685852050781, 178.67984008789062)
    vector_math_002.location = (178.7374267578125, -32.26443099975586)
    vector_math_001_1.location = (414.91314697265625, 69.62020874023438)
    math_1.location = (610.6982421875, 58.64157485961914)
    texture_coordinate_001.location = (-1001.3757934570312, 180.7987060546875)
    vector_math_004.location = (-560.58447265625, 7.026371002197266)
    vector_math_005.location = (-114.8895263671875, 28.198429107666016)
    vector_math_003.location = (-132.23243713378906, -206.68572998046875)
    combine_xyz_1.location = (-686.55126953125, -363.2596740722656)
    vector_math_011.location = (-781.0, 53.531402587890625)
    group_input_1.location = (-1496.9405517578125, -527.56689453125)
    separate_xyz_001.location = (110.30845642089844, 623.1296997070312)
    vector_math_007.location = (456.2660217285156, 514.070068359375)
    texture_coordinate_002.location = (-976.3941650390625, 625.2485961914062)
    vector_math_006.location = (220.09030151367188, 412.1854248046875)
    vector_math_1.location = (-35.14213562011719, 386.2591247558594)
    vector_math_009.location = (-216.7398681640625, 455.4271240234375)
    math_004.location = (686.32861328125, 513.2443237304688)
    group_input_001_1.location = (320.343994140625, 651.840576171875)
    math_002_1.location = (855.4006958007812, 445.6868896484375)
    vector_math_008.location = (-519.2316284179688, 451.4762268066406)
    vector_math_012.location = (-1079.423095703125, 379.7279052734375)
    vector_math_010.location = (-739.6287231445312, 437.7539978027344)
    vector_math_013_1.location = (-746.6356201171875, 1251.9586181640625)
    vector_math_014_1.location = (-406.8412780761719, 1309.9847412109375)
    group_input_003_1.location = (95.8216781616211, 1042.517333984375)
    math_003_1.location = (1161.345947265625, 231.27822875976562)
    group_output_1.location = (2172.580322265625, 1214.2205810546875)
    math_005_1.location = (1732.6168212890625, 1075.495849609375)
    math_006_1.location = (1953.0, 1197.583251953125)
    group_input_005.location = (1144.3414306640625, 1329.0762939453125)
    group_input_004_1.location = (-1049.4193115234375, 1310.19091796875)
    uv_map.location = (-1175.9093017578125, -56.09785461425781)
    group.location = (1484.0780029296875, 1179.138916015625)
    group_input_002_1.location = (-1497.2548828125, 182.37332153320312)

    #Set dimensions
    math_001_1.width, math_001_1.height = 140.0, 100.0
    map_range.width, map_range.height = 140.0, 100.0
    separate_xyz_1.width, separate_xyz_1.height = 140.0, 100.0
    vector_math_002.width, vector_math_002.height = 140.0, 100.0
    vector_math_001_1.width, vector_math_001_1.height = 140.0, 100.0
    math_1.width, math_1.height = 140.0, 100.0
    texture_coordinate_001.width, texture_coordinate_001.height = 140.0, 100.0
    vector_math_004.width, vector_math_004.height = 140.0, 100.0
    vector_math_005.width, vector_math_005.height = 140.0, 100.0
    vector_math_003.width, vector_math_003.height = 140.0, 100.0
    combine_xyz_1.width, combine_xyz_1.height = 140.0, 100.0
    vector_math_011.width, vector_math_011.height = 140.0, 100.0
    group_input_1.width, group_input_1.height = 183.0322265625, 100.0
    separate_xyz_001.width, separate_xyz_001.height = 140.0, 100.0
    vector_math_007.width, vector_math_007.height = 140.0, 100.0
    texture_coordinate_002.width, texture_coordinate_002.height = 140.0, 100.0
    vector_math_006.width, vector_math_006.height = 140.0, 100.0
    vector_math_1.width, vector_math_1.height = 140.0, 100.0
    vector_math_009.width, vector_math_009.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    group_input_001_1.width, group_input_001_1.height = 183.0322265625, 100.0
    math_002_1.width, math_002_1.height = 140.0, 100.0
    vector_math_008.width, vector_math_008.height = 140.0, 100.0
    vector_math_012.width, vector_math_012.height = 140.0, 100.0
    vector_math_010.width, vector_math_010.height = 140.0, 100.0
    vector_math_013_1.width, vector_math_013_1.height = 140.0, 100.0
    vector_math_014_1.width, vector_math_014_1.height = 140.0, 100.0
    group_input_003_1.width, group_input_003_1.height = 183.0322265625, 100.0
    math_003_1.width, math_003_1.height = 140.0, 100.0
    group_output_1.width, group_output_1.height = 140.0, 100.0
    math_005_1.width, math_005_1.height = 140.0, 100.0
    math_006_1.width, math_006_1.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    group_input_004_1.width, group_input_004_1.height = 183.0322265625, 100.0
    uv_map.width, uv_map.height = 150.0, 100.0
    group.width, group.height = 140.0, 100.0
    group_input_002_1.width, group_input_002_1.height = 183.0322265625, 100.0

    #initialize eye links
    #vector_math_002.Vector -> vector_math_001_1.Vector
    eye.links.new(vector_math_002.outputs[0], vector_math_001_1.inputs[0])
    #vector_math_004.Vector -> vector_math_003.Vector
    eye.links.new(vector_math_004.outputs[0], vector_math_003.inputs[0])
    #vector_math_001_1.Value -> math_1.Value
    eye.links.new(vector_math_001_1.outputs[1], math_1.inputs[0])
    #vector_math_011.Vector -> vector_math_004.Vector
    eye.links.new(vector_math_011.outputs[0], vector_math_004.inputs[0])
    #vector_math_005.Vector -> vector_math_002.Vector
    eye.links.new(vector_math_005.outputs[0], vector_math_002.inputs[0])
    #vector_math_004.Vector -> vector_math_005.Vector
    eye.links.new(vector_math_004.outputs[0], vector_math_005.inputs[0])
    #combine_xyz_1.Vector -> vector_math_005.Vector
    eye.links.new(combine_xyz_1.outputs[0], vector_math_005.inputs[1])
    #group_input_1.Eye -> map_range.Value
    eye.links.new(group_input_1.outputs[1], map_range.inputs[0])
    #map_range.Result -> math_001_1.Value
    eye.links.new(map_range.outputs[0], math_001_1.inputs[0])
    #math_001_1.Value -> combine_xyz_1.X
    eye.links.new(math_001_1.outputs[0], combine_xyz_1.inputs[0])
    #group_input_1.X -> math_001_1.Value
    eye.links.new(group_input_1.outputs[0], math_001_1.inputs[1])
    #vector_math_006.Vector -> vector_math_007.Vector
    eye.links.new(vector_math_006.outputs[0], vector_math_007.inputs[0])
    #vector_math_010.Vector -> vector_math_008.Vector
    eye.links.new(vector_math_010.outputs[0], vector_math_008.inputs[0])
    #vector_math_008.Vector -> vector_math_009.Vector
    eye.links.new(vector_math_008.outputs[0], vector_math_009.inputs[0])
    #math_1.Value -> math_003_1.Value
    eye.links.new(math_1.outputs[0], math_003_1.inputs[1])
    #combine_xyz_1.Vector -> vector_math_009.Vector
    eye.links.new(combine_xyz_1.outputs[0], vector_math_009.inputs[1])
    #vector_math_009.Vector -> vector_math_1.Vector
    eye.links.new(vector_math_009.outputs[0], vector_math_1.inputs[0])
    #vector_math_009.Vector -> vector_math_006.Vector
    eye.links.new(vector_math_009.outputs[0], vector_math_006.inputs[0])
    #math_004.Value -> math_002_1.Value
    eye.links.new(math_004.outputs[0], math_002_1.inputs[0])
    #group_input_001_1.Pupil Size -> math_004.Value
    eye.links.new(group_input_001_1.outputs[2], math_004.inputs[1])
    #vector_math_007.Value -> math_004.Value
    eye.links.new(vector_math_007.outputs[1], math_004.inputs[0])
    #math_002_1.Value -> math_003_1.Value
    eye.links.new(math_002_1.outputs[0], math_003_1.inputs[0])
    #group_input_002_1.Eye Offset -> vector_math_011.Vector
    eye.links.new(group_input_002_1.outputs[3], vector_math_011.inputs[1])
    #vector_math_012.Vector -> vector_math_010.Vector
    eye.links.new(vector_math_012.outputs[0], vector_math_010.inputs[1])
    #group_input_002_1.Eye Offset -> vector_math_012.Vector
    eye.links.new(group_input_002_1.outputs[3], vector_math_012.inputs[0])
    #group_input_002_1.Pupil Offset -> vector_math_012.Vector
    eye.links.new(group_input_002_1.outputs[4], vector_math_012.inputs[1])
    #vector_math_013_1.Vector -> vector_math_014_1.Vector
    eye.links.new(vector_math_013_1.outputs[0], vector_math_014_1.inputs[1])
    #group_input_004_1.Eye Offset -> vector_math_013_1.Vector
    eye.links.new(group_input_004_1.outputs[3], vector_math_013_1.inputs[0])
    #vector_math_014_1.Vector -> group.Vector
    eye.links.new(vector_math_014_1.outputs[0], group.inputs[0])
    #combine_xyz_1.Vector -> group.Vector
    eye.links.new(combine_xyz_1.outputs[0], group.inputs[1])
    #math_003_1.Value -> math_005_1.Value
    eye.links.new(math_003_1.outputs[0], math_005_1.inputs[1])
    #math_006_1.Value -> group_output_1.Value
    eye.links.new(math_006_1.outputs[0], group_output_1.inputs[0])
    #group.Value -> math_005_1.Value
    eye.links.new(group.outputs[1], math_005_1.inputs[0])
    #math_005_1.Value -> math_006_1.Value
    eye.links.new(math_005_1.outputs[0], math_006_1.inputs[1])
    #group.Value -> math_006_1.Value
    eye.links.new(group.outputs[0], math_006_1.inputs[0])
    #group_input_005.Eyebrow Flatness -> group.Flatness
    eye.links.new(group_input_005.outputs[5], group.inputs[2])
    #group_input_005.EyeBrow Size -> group.Size
    eye.links.new(group_input_005.outputs[6], group.inputs[3])
    #group_input_005.Eyebrow angle -> group.Angle
    eye.links.new(group_input_005.outputs[7], group.inputs[4])
    #group_input_005.EyeBrow height -> group.Height
    eye.links.new(group_input_005.outputs[8], group.inputs[5])
    #group_input_002_1.UV -> vector_math_011.Vector
    eye.links.new(group_input_002_1.outputs[9], vector_math_011.inputs[0])
    #group_input_002_1.UV -> separate_xyz_1.Vector
    eye.links.new(group_input_002_1.outputs[9], separate_xyz_1.inputs[0])
    #group_input_002_1.UV -> vector_math_010.Vector
    eye.links.new(group_input_002_1.outputs[9], vector_math_010.inputs[0])
    #group_input_002_1.UV -> separate_xyz_001.Vector
    eye.links.new(group_input_002_1.outputs[9], separate_xyz_001.inputs[0])
    #group_input_002_1.UV -> group.Vector
    eye.links.new(group_input_002_1.outputs[9], group.inputs[6])
    return eye

eye = eye_node_group()

#initialize Double Eye -Internal Join node group
def double_eye__internal_join_node_group():

    double_eye__internal_join = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "Double Eye -Internal Join")

    double_eye__internal_join.color_tag = 'NONE'
    double_eye__internal_join.description = ""
    double_eye__internal_join.default_group_node_width = 140
    

    #double_eye__internal_join interface
    #Socket Value
    value_socket_3 = double_eye__internal_join.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    value_socket_3.default_value = 0.0
    value_socket_3.min_value = -3.4028234663852886e+38
    value_socket_3.max_value = 3.4028234663852886e+38
    value_socket_3.subtype = 'NONE'
    value_socket_3.attribute_domain = 'POINT'

    #Socket Pupil Size
    pupil_size_socket_1 = double_eye__internal_join.interface.new_socket(name = "Pupil Size", in_out='INPUT', socket_type = 'NodeSocketFloat')
    pupil_size_socket_1.default_value = 0.15000000596046448
    pupil_size_socket_1.min_value = -3.4028234663852886e+38
    pupil_size_socket_1.max_value = 3.4028234663852886e+38
    pupil_size_socket_1.subtype = 'NONE'
    pupil_size_socket_1.attribute_domain = 'POINT'

    #Socket Seperation
    seperation_socket = double_eye__internal_join.interface.new_socket(name = "Seperation", in_out='INPUT', socket_type = 'NodeSocketFloat')
    seperation_socket.default_value = 0.20000000298023224
    seperation_socket.min_value = -10000.0
    seperation_socket.max_value = 10000.0
    seperation_socket.subtype = 'NONE'
    seperation_socket.attribute_domain = 'POINT'

    #Socket Eye Offset
    eye_offset_socket_1 = double_eye__internal_join.interface.new_socket(name = "Eye Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
    eye_offset_socket_1.default_value = (0.0, 0.0, 0.0)
    eye_offset_socket_1.min_value = -10000.0
    eye_offset_socket_1.max_value = 10000.0
    eye_offset_socket_1.subtype = 'NONE'
    eye_offset_socket_1.attribute_domain = 'POINT'

    #Socket Pupil Offset
    pupil_offset_socket_1 = double_eye__internal_join.interface.new_socket(name = "Pupil Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
    pupil_offset_socket_1.default_value = (0.0, 0.0, 0.0)
    pupil_offset_socket_1.min_value = -10000.0
    pupil_offset_socket_1.max_value = 10000.0
    pupil_offset_socket_1.subtype = 'NONE'
    pupil_offset_socket_1.attribute_domain = 'POINT'

    #Socket Left Pupil Offset
    left_pupil_offset_socket = double_eye__internal_join.interface.new_socket(name = "Left Pupil Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
    left_pupil_offset_socket.default_value = (0.0, 0.0, 0.0)
    left_pupil_offset_socket.min_value = -10000.0
    left_pupil_offset_socket.max_value = 10000.0
    left_pupil_offset_socket.subtype = 'NONE'
    left_pupil_offset_socket.attribute_domain = 'POINT'

    #Socket Right Pupil Offset
    right_pupil_offset_socket = double_eye__internal_join.interface.new_socket(name = "Right Pupil Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
    right_pupil_offset_socket.default_value = (0.0, 0.0, 0.0)
    right_pupil_offset_socket.min_value = -10000.0
    right_pupil_offset_socket.max_value = 10000.0
    right_pupil_offset_socket.subtype = 'NONE'
    right_pupil_offset_socket.attribute_domain = 'POINT'

    #Socket Left Eye Offset
    left_eye_offset_socket = double_eye__internal_join.interface.new_socket(name = "Left Eye Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
    left_eye_offset_socket.default_value = (0.0, 0.0, 0.0)
    left_eye_offset_socket.min_value = -10000.0
    left_eye_offset_socket.max_value = 10000.0
    left_eye_offset_socket.subtype = 'NONE'
    left_eye_offset_socket.attribute_domain = 'POINT'

    #Socket Right Eye Offset
    right_eye_offset_socket = double_eye__internal_join.interface.new_socket(name = "Right Eye Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
    right_eye_offset_socket.default_value = (0.0, 0.0, 0.0)
    right_eye_offset_socket.min_value = -10000.0
    right_eye_offset_socket.max_value = 10000.0
    right_eye_offset_socket.subtype = 'NONE'
    right_eye_offset_socket.attribute_domain = 'POINT'

    #Socket Left Eyebrow Flatness
    left_eyebrow_flatness_socket = double_eye__internal_join.interface.new_socket(name = "Left Eyebrow Flatness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    left_eyebrow_flatness_socket.default_value = 0.20000052452087402
    left_eyebrow_flatness_socket.min_value = 0.0
    left_eyebrow_flatness_socket.max_value = 10000.0
    left_eyebrow_flatness_socket.subtype = 'NONE'
    left_eyebrow_flatness_socket.attribute_domain = 'POINT'

    #Socket Left EyeBrow Size
    left_eyebrow_size_socket = double_eye__internal_join.interface.new_socket(name = "Left EyeBrow Size", in_out='INPUT', socket_type = 'NodeSocketFloat')
    left_eyebrow_size_socket.default_value = 0.10000000149011612
    left_eyebrow_size_socket.min_value = -3.4028234663852886e+38
    left_eyebrow_size_socket.max_value = 3.4028234663852886e+38
    left_eyebrow_size_socket.subtype = 'NONE'
    left_eyebrow_size_socket.attribute_domain = 'POINT'

    #Socket Left Eyebrow angle
    left_eyebrow_angle_socket = double_eye__internal_join.interface.new_socket(name = "Left Eyebrow angle", in_out='INPUT', socket_type = 'NodeSocketFloat')
    left_eyebrow_angle_socket.default_value = 0.179768905043602
    left_eyebrow_angle_socket.min_value = -3.4028234663852886e+38
    left_eyebrow_angle_socket.max_value = 3.4028234663852886e+38
    left_eyebrow_angle_socket.subtype = 'ANGLE'
    left_eyebrow_angle_socket.attribute_domain = 'POINT'

    #Socket left EyeBrow height
    left_eyebrow_height_socket = double_eye__internal_join.interface.new_socket(name = "left EyeBrow height", in_out='INPUT', socket_type = 'NodeSocketFloat')
    left_eyebrow_height_socket.default_value = -0.10000000149011612
    left_eyebrow_height_socket.min_value = -10000.0
    left_eyebrow_height_socket.max_value = 10000.0
    left_eyebrow_height_socket.subtype = 'NONE'
    left_eyebrow_height_socket.attribute_domain = 'POINT'

    #Socket Right Eyebrow Flatnessa
    right_eyebrow_flatnessa_socket = double_eye__internal_join.interface.new_socket(name = "Right Eyebrow Flatnessa", in_out='INPUT', socket_type = 'NodeSocketFloat')
    right_eyebrow_flatnessa_socket.default_value = 0.20000052452087402
    right_eyebrow_flatnessa_socket.min_value = 0.0
    right_eyebrow_flatnessa_socket.max_value = 10000.0
    right_eyebrow_flatnessa_socket.subtype = 'NONE'
    right_eyebrow_flatnessa_socket.attribute_domain = 'POINT'

    #Socket right EyeBrow Size
    right_eyebrow_size_socket = double_eye__internal_join.interface.new_socket(name = "right EyeBrow Size", in_out='INPUT', socket_type = 'NodeSocketFloat')
    right_eyebrow_size_socket.default_value = 0.09999999403953552
    right_eyebrow_size_socket.min_value = -3.4028234663852886e+38
    right_eyebrow_size_socket.max_value = 3.4028234663852886e+38
    right_eyebrow_size_socket.subtype = 'NONE'
    right_eyebrow_size_socket.attribute_domain = 'POINT'

    #Socket Right Eyebrow angle
    right_eyebrow_angle_socket = double_eye__internal_join.interface.new_socket(name = "Right Eyebrow angle", in_out='INPUT', socket_type = 'NodeSocketFloat')
    right_eyebrow_angle_socket.default_value = -0.1745329201221466
    right_eyebrow_angle_socket.min_value = -3.4028234663852886e+38
    right_eyebrow_angle_socket.max_value = 3.4028234663852886e+38
    right_eyebrow_angle_socket.subtype = 'ANGLE'
    right_eyebrow_angle_socket.attribute_domain = 'POINT'

    #Socket Right EyeBrow height
    right_eyebrow_height_socket = double_eye__internal_join.interface.new_socket(name = "Right EyeBrow height", in_out='INPUT', socket_type = 'NodeSocketFloat')
    right_eyebrow_height_socket.default_value = -0.10000000149011612
    right_eyebrow_height_socket.min_value = -10000.0
    right_eyebrow_height_socket.max_value = 10000.0
    right_eyebrow_height_socket.subtype = 'NONE'
    right_eyebrow_height_socket.attribute_domain = 'POINT'


    #initialize double_eye__internal_join nodes
    #node Clamp
    clamp = double_eye__internal_join.nodes.new("ShaderNodeClamp")
    clamp.name = "Clamp"
    clamp.clamp_type = 'MINMAX'
    #Min
    clamp.inputs[1].default_value = 0.0010000000474974513
    #Max
    clamp.inputs[2].default_value = 0.8999999761581421

    #node Vector Math.001
    vector_math_001_2 = double_eye__internal_join.nodes.new("ShaderNodeVectorMath")
    vector_math_001_2.name = "Vector Math.001"
    vector_math_001_2.operation = 'ADD'

    #node Vector Math.003
    vector_math_003_1 = double_eye__internal_join.nodes.new("ShaderNodeVectorMath")
    vector_math_003_1.name = "Vector Math.003"
    vector_math_003_1.operation = 'ADD'

    #node Vector Math.002
    vector_math_002_1 = double_eye__internal_join.nodes.new("ShaderNodeVectorMath")
    vector_math_002_1.name = "Vector Math.002"
    vector_math_002_1.operation = 'ADD'

    #node Vector Math
    vector_math_2 = double_eye__internal_join.nodes.new("ShaderNodeVectorMath")
    vector_math_2.name = "Vector Math"
    vector_math_2.operation = 'ADD'

    #node Group Input
    group_input_2 = double_eye__internal_join.nodes.new("NodeGroupInput")
    group_input_2.name = "Group Input"

    #node Math
    math_2 = double_eye__internal_join.nodes.new("ShaderNodeMath")
    math_2.name = "Math"
    math_2.operation = 'ADD'
    math_2.use_clamp = False

    #node Group Output
    group_output_2 = double_eye__internal_join.nodes.new("NodeGroupOutput")
    group_output_2.name = "Group Output"
    group_output_2.is_active_output = True

    #node Group.001
    group_001 = double_eye__internal_join.nodes.new("ShaderNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = eye
    #Input_2
    group_001.inputs[1].default_value = 1.0

    #node Group Input.001
    group_input_001_2 = double_eye__internal_join.nodes.new("NodeGroupInput")
    group_input_001_2.name = "Group Input.001"

    #node Group Input.002
    group_input_002_2 = double_eye__internal_join.nodes.new("NodeGroupInput")
    group_input_002_2.name = "Group Input.002"

    #node UV Map
    uv_map_1 = double_eye__internal_join.nodes.new("ShaderNodeUVMap")
    uv_map_1.name = "UV Map"
    uv_map_1.from_instancer = False
    uv_map_1.uv_map = "UVMap"

    #node Group
    group_1 = double_eye__internal_join.nodes.new("ShaderNodeGroup")
    group_1.name = "Group"
    group_1.node_tree = eye
    #Input_2
    group_1.inputs[1].default_value = 0.0


    #Set locations
    clamp.location = (660.0756225585938, -19.600543975830078)
    vector_math_001_2.location = (-5.432853698730469, 291.263671875)
    vector_math_003_1.location = (-9.178430557250977, 93.62138366699219)
    vector_math_002_1.location = (23.412670135498047, -497.5614013671875)
    vector_math_2.location = (29.86432456970215, -364.3374328613281)
    group_input_2.location = (-591.4750366210938, -113.53626251220703)
    math_2.location = (1745.029052734375, -29.06551170349121)
    group_output_2.location = (1935.029052734375, 29.700176239013672)
    group_001.location = (924.7716674804688, -356.1051025390625)
    group_input_001_2.location = (453.92724609375, -590.4852905273438)
    group_input_002_2.location = (506.79345703125, 582.9090576171875)
    uv_map_1.location = (371.67327880859375, -175.4871826171875)
    group_1.location = (940.8203125, 287.341796875)

    #Set dimensions
    clamp.width, clamp.height = 140.0, 100.0
    vector_math_001_2.width, vector_math_001_2.height = 140.0, 100.0
    vector_math_003_1.width, vector_math_003_1.height = 140.0, 100.0
    vector_math_002_1.width, vector_math_002_1.height = 140.0, 100.0
    vector_math_2.width, vector_math_2.height = 140.0, 100.0
    group_input_2.width, group_input_2.height = 140.0, 100.0
    math_2.width, math_2.height = 140.0, 100.0
    group_output_2.width, group_output_2.height = 140.0, 100.0
    group_001.width, group_001.height = 235.04150390625, 100.0
    group_input_001_2.width, group_input_001_2.height = 140.0, 100.0
    group_input_002_2.width, group_input_002_2.height = 167.9273681640625, 100.0
    uv_map_1.width, uv_map_1.height = 150.0, 100.0
    group_1.width, group_1.height = 140.0, 100.0

    #initialize double_eye__internal_join links
    #math_2.Value -> group_output_2.Value
    double_eye__internal_join.links.new(math_2.outputs[0], group_output_2.inputs[0])
    #group_001.Value -> math_2.Value
    double_eye__internal_join.links.new(group_001.outputs[0], math_2.inputs[1])
    #group_1.Value -> math_2.Value
    double_eye__internal_join.links.new(group_1.outputs[0], math_2.inputs[0])
    #clamp.Result -> group_001.Pupil Size
    double_eye__internal_join.links.new(clamp.outputs[0], group_001.inputs[2])
    #clamp.Result -> group_1.Pupil Size
    double_eye__internal_join.links.new(clamp.outputs[0], group_1.inputs[2])
    #group_input_2.Pupil Size -> clamp.Value
    double_eye__internal_join.links.new(group_input_2.outputs[0], clamp.inputs[0])
    #group_input_2.Seperation -> group_1.X
    double_eye__internal_join.links.new(group_input_2.outputs[1], group_1.inputs[0])
    #group_input_2.Seperation -> group_001.X
    double_eye__internal_join.links.new(group_input_2.outputs[1], group_001.inputs[0])
    #group_input_2.Pupil Offset -> vector_math_2.Vector
    double_eye__internal_join.links.new(group_input_2.outputs[3], vector_math_2.inputs[0])
    #group_input_2.Left Pupil Offset -> vector_math_2.Vector
    double_eye__internal_join.links.new(group_input_2.outputs[4], vector_math_2.inputs[1])
    #group_input_2.Pupil Offset -> vector_math_001_2.Vector
    double_eye__internal_join.links.new(group_input_2.outputs[3], vector_math_001_2.inputs[0])
    #group_input_2.Right Pupil Offset -> vector_math_001_2.Vector
    double_eye__internal_join.links.new(group_input_2.outputs[5], vector_math_001_2.inputs[1])
    #group_input_2.Eye Offset -> vector_math_002_1.Vector
    double_eye__internal_join.links.new(group_input_2.outputs[2], vector_math_002_1.inputs[0])
    #group_input_2.Left Eye Offset -> vector_math_002_1.Vector
    double_eye__internal_join.links.new(group_input_2.outputs[6], vector_math_002_1.inputs[1])
    #group_input_2.Eye Offset -> vector_math_003_1.Vector
    double_eye__internal_join.links.new(group_input_2.outputs[2], vector_math_003_1.inputs[0])
    #vector_math_001_2.Vector -> group_1.Eye Offset
    double_eye__internal_join.links.new(vector_math_001_2.outputs[0], group_1.inputs[3])
    #vector_math_003_1.Vector -> group_1.Pupil Offset
    double_eye__internal_join.links.new(vector_math_003_1.outputs[0], group_1.inputs[4])
    #group_input_2.Right Eye Offset -> vector_math_003_1.Vector
    double_eye__internal_join.links.new(group_input_2.outputs[7], vector_math_003_1.inputs[1])
    #vector_math_002_1.Vector -> group_001.Pupil Offset
    double_eye__internal_join.links.new(vector_math_002_1.outputs[0], group_001.inputs[4])
    #vector_math_2.Vector -> group_001.Eye Offset
    double_eye__internal_join.links.new(vector_math_2.outputs[0], group_001.inputs[3])
    #group_input_001_2.Left Eyebrow Flatness -> group_001.Eyebrow Flatness
    double_eye__internal_join.links.new(group_input_001_2.outputs[8], group_001.inputs[5])
    #group_input_001_2.Left EyeBrow Size -> group_001.EyeBrow Size
    double_eye__internal_join.links.new(group_input_001_2.outputs[9], group_001.inputs[6])
    #group_input_001_2.Left Eyebrow angle -> group_001.Eyebrow angle
    double_eye__internal_join.links.new(group_input_001_2.outputs[10], group_001.inputs[7])
    #group_input_001_2.left EyeBrow height -> group_001.EyeBrow height
    double_eye__internal_join.links.new(group_input_001_2.outputs[11], group_001.inputs[8])
    #group_input_002_2.Right Eyebrow Flatnessa -> group_1.Eyebrow Flatness
    double_eye__internal_join.links.new(group_input_002_2.outputs[12], group_1.inputs[5])
    #group_input_002_2.right EyeBrow Size -> group_1.EyeBrow Size
    double_eye__internal_join.links.new(group_input_002_2.outputs[13], group_1.inputs[6])
    #group_input_002_2.Right Eyebrow angle -> group_1.Eyebrow angle
    double_eye__internal_join.links.new(group_input_002_2.outputs[14], group_1.inputs[7])
    #group_input_002_2.Right EyeBrow height -> group_1.EyeBrow height
    double_eye__internal_join.links.new(group_input_002_2.outputs[15], group_1.inputs[8])
    #uv_map_1.UV -> group_1.UV
    double_eye__internal_join.links.new(uv_map_1.outputs[0], group_1.inputs[9])
    #uv_map_1.UV -> group_001.UV
    double_eye__internal_join.links.new(uv_map_1.outputs[0], group_001.inputs[9])
    return double_eye__internal_join

double_eye__internal_join = double_eye__internal_join_node_group()

#initialize Drone Eyes node group
def drone_eyes_node_group():

    drone_eyes = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "Drone Eyes")

    drone_eyes.color_tag = 'NONE'
    drone_eyes.description = ""
    drone_eyes.default_group_node_width = 140
    

    #drone_eyes interface
    #Socket Value
    value_socket_4 = drone_eyes.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    value_socket_4.default_value = 0.0
    value_socket_4.min_value = -3.4028234663852886e+38
    value_socket_4.max_value = 3.4028234663852886e+38
    value_socket_4.subtype = 'NONE'
    value_socket_4.attribute_domain = 'POINT'

    #Socket Pupil Size
    pupil_size_socket_2 = drone_eyes.interface.new_socket(name = "Pupil Size", in_out='INPUT', socket_type = 'NodeSocketFloat')
    pupil_size_socket_2.default_value = 0.15000000596046448
    pupil_size_socket_2.min_value = -3.4028234663852886e+38
    pupil_size_socket_2.max_value = 3.4028234663852886e+38
    pupil_size_socket_2.subtype = 'NONE'
    pupil_size_socket_2.attribute_domain = 'POINT'

    #Socket Seperation
    seperation_socket_1 = drone_eyes.interface.new_socket(name = "Seperation", in_out='INPUT', socket_type = 'NodeSocketFloat')
    seperation_socket_1.default_value = 0.20000000298023224
    seperation_socket_1.min_value = -10000.0
    seperation_socket_1.max_value = 10000.0
    seperation_socket_1.subtype = 'NONE'
    seperation_socket_1.attribute_domain = 'POINT'

    #Socket Eye Offset
    eye_offset_socket_2 = drone_eyes.interface.new_socket(name = "Eye Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
    eye_offset_socket_2.default_value = (0.0, 0.0, 0.0)
    eye_offset_socket_2.min_value = -10000.0
    eye_offset_socket_2.max_value = 10000.0
    eye_offset_socket_2.subtype = 'NONE'
    eye_offset_socket_2.attribute_domain = 'POINT'

    #Socket Pupil Offset
    pupil_offset_socket_2 = drone_eyes.interface.new_socket(name = "Pupil Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
    pupil_offset_socket_2.default_value = (0.0, 0.0, 0.0)
    pupil_offset_socket_2.min_value = -10000.0
    pupil_offset_socket_2.max_value = 10000.0
    pupil_offset_socket_2.subtype = 'NONE'
    pupil_offset_socket_2.attribute_domain = 'POINT'

    #Socket Left Pupil Offset
    left_pupil_offset_socket_1 = drone_eyes.interface.new_socket(name = "Left Pupil Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
    left_pupil_offset_socket_1.default_value = (0.0, 0.0, 0.0)
    left_pupil_offset_socket_1.min_value = -10000.0
    left_pupil_offset_socket_1.max_value = 10000.0
    left_pupil_offset_socket_1.subtype = 'NONE'
    left_pupil_offset_socket_1.attribute_domain = 'POINT'

    #Socket Right Pupil Offset
    right_pupil_offset_socket_1 = drone_eyes.interface.new_socket(name = "Right Pupil Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
    right_pupil_offset_socket_1.default_value = (0.0, 0.0, 0.0)
    right_pupil_offset_socket_1.min_value = -10000.0
    right_pupil_offset_socket_1.max_value = 10000.0
    right_pupil_offset_socket_1.subtype = 'NONE'
    right_pupil_offset_socket_1.attribute_domain = 'POINT'

    #Socket Left Eye Offset
    left_eye_offset_socket_1 = drone_eyes.interface.new_socket(name = "Left Eye Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
    left_eye_offset_socket_1.default_value = (0.0, 0.0, 0.0)
    left_eye_offset_socket_1.min_value = -10000.0
    left_eye_offset_socket_1.max_value = 10000.0
    left_eye_offset_socket_1.subtype = 'NONE'
    left_eye_offset_socket_1.attribute_domain = 'POINT'

    #Socket Right Eye Offset
    right_eye_offset_socket_1 = drone_eyes.interface.new_socket(name = "Right Eye Offset", in_out='INPUT', socket_type = 'NodeSocketVector')
    right_eye_offset_socket_1.default_value = (0.0, 0.0, 0.0)
    right_eye_offset_socket_1.min_value = -10000.0
    right_eye_offset_socket_1.max_value = 10000.0
    right_eye_offset_socket_1.subtype = 'NONE'
    right_eye_offset_socket_1.attribute_domain = 'POINT'

    #Socket Eyebrow flatness
    eyebrow_flatness_socket_1 = drone_eyes.interface.new_socket(name = "Eyebrow flatness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    eyebrow_flatness_socket_1.default_value = 0.5
    eyebrow_flatness_socket_1.min_value = -10000.0
    eyebrow_flatness_socket_1.max_value = 10000.0
    eyebrow_flatness_socket_1.subtype = 'NONE'
    eyebrow_flatness_socket_1.attribute_domain = 'POINT'

    #Socket Eyebrow Size
    eyebrow_size_socket_1 = drone_eyes.interface.new_socket(name = "Eyebrow Size", in_out='INPUT', socket_type = 'NodeSocketFloat')
    eyebrow_size_socket_1.default_value = 0.10000000149011612
    eyebrow_size_socket_1.min_value = -10000.0
    eyebrow_size_socket_1.max_value = 10000.0
    eyebrow_size_socket_1.subtype = 'NONE'
    eyebrow_size_socket_1.attribute_domain = 'POINT'

    #Socket Eyebrow angle
    eyebrow_angle_socket_1 = drone_eyes.interface.new_socket(name = "Eyebrow angle", in_out='INPUT', socket_type = 'NodeSocketFloat')
    eyebrow_angle_socket_1.default_value = 0.179768905043602
    eyebrow_angle_socket_1.min_value = -3.4028234663852886e+38
    eyebrow_angle_socket_1.max_value = 3.4028234663852886e+38
    eyebrow_angle_socket_1.subtype = 'ANGLE'
    eyebrow_angle_socket_1.attribute_domain = 'POINT'

    #Socket EyeBrow height
    eyebrow_height_socket_1 = drone_eyes.interface.new_socket(name = "EyeBrow height", in_out='INPUT', socket_type = 'NodeSocketFloat')
    eyebrow_height_socket_1.default_value = -0.10000000149011612
    eyebrow_height_socket_1.min_value = -10000.0
    eyebrow_height_socket_1.max_value = 10000.0
    eyebrow_height_socket_1.subtype = 'NONE'
    eyebrow_height_socket_1.attribute_domain = 'POINT'

    #Socket Left Eyebrow Flatness
    left_eyebrow_flatness_socket_1 = drone_eyes.interface.new_socket(name = "Left Eyebrow Flatness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    left_eyebrow_flatness_socket_1.default_value = 0.0
    left_eyebrow_flatness_socket_1.min_value = -10000.0
    left_eyebrow_flatness_socket_1.max_value = 10000.0
    left_eyebrow_flatness_socket_1.subtype = 'NONE'
    left_eyebrow_flatness_socket_1.attribute_domain = 'POINT'

    #Socket Left Eyebrow Size
    left_eyebrow_size_socket_1 = drone_eyes.interface.new_socket(name = "Left Eyebrow Size", in_out='INPUT', socket_type = 'NodeSocketFloat')
    left_eyebrow_size_socket_1.default_value = 0.0
    left_eyebrow_size_socket_1.min_value = -10000.0
    left_eyebrow_size_socket_1.max_value = 10000.0
    left_eyebrow_size_socket_1.subtype = 'NONE'
    left_eyebrow_size_socket_1.attribute_domain = 'POINT'

    #Socket Left Eyebrow Angle
    left_eyebrow_angle_socket_1 = drone_eyes.interface.new_socket(name = "Left Eyebrow Angle", in_out='INPUT', socket_type = 'NodeSocketFloat')
    left_eyebrow_angle_socket_1.default_value = 0.0
    left_eyebrow_angle_socket_1.min_value = -10000.0
    left_eyebrow_angle_socket_1.max_value = 10000.0
    left_eyebrow_angle_socket_1.subtype = 'NONE'
    left_eyebrow_angle_socket_1.attribute_domain = 'POINT'

    #Socket Left Eyebrow Height
    left_eyebrow_height_socket_1 = drone_eyes.interface.new_socket(name = "Left Eyebrow Height", in_out='INPUT', socket_type = 'NodeSocketFloat')
    left_eyebrow_height_socket_1.default_value = 0.0
    left_eyebrow_height_socket_1.min_value = -10000.0
    left_eyebrow_height_socket_1.max_value = 10000.0
    left_eyebrow_height_socket_1.subtype = 'NONE'
    left_eyebrow_height_socket_1.attribute_domain = 'POINT'

    #Socket Right Eyebrow Flatness
    right_eyebrow_flatness_socket = drone_eyes.interface.new_socket(name = "Right Eyebrow Flatness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    right_eyebrow_flatness_socket.default_value = 0.0
    right_eyebrow_flatness_socket.min_value = -10000.0
    right_eyebrow_flatness_socket.max_value = 10000.0
    right_eyebrow_flatness_socket.subtype = 'NONE'
    right_eyebrow_flatness_socket.attribute_domain = 'POINT'

    #Socket Eight Eyebrow Size
    eight_eyebrow_size_socket = drone_eyes.interface.new_socket(name = "Eight Eyebrow Size", in_out='INPUT', socket_type = 'NodeSocketFloat')
    eight_eyebrow_size_socket.default_value = 0.0
    eight_eyebrow_size_socket.min_value = -10000.0
    eight_eyebrow_size_socket.max_value = 10000.0
    eight_eyebrow_size_socket.subtype = 'NONE'
    eight_eyebrow_size_socket.attribute_domain = 'POINT'

    #Socket Right Eyebrow Angle
    right_eyebrow_angle_socket_1 = drone_eyes.interface.new_socket(name = "Right Eyebrow Angle", in_out='INPUT', socket_type = 'NodeSocketFloat')
    right_eyebrow_angle_socket_1.default_value = 0.0
    right_eyebrow_angle_socket_1.min_value = -10000.0
    right_eyebrow_angle_socket_1.max_value = 10000.0
    right_eyebrow_angle_socket_1.subtype = 'NONE'
    right_eyebrow_angle_socket_1.attribute_domain = 'POINT'

    #Socket Right Eyebrow Height
    right_eyebrow_height_socket_1 = drone_eyes.interface.new_socket(name = "Right Eyebrow Height", in_out='INPUT', socket_type = 'NodeSocketFloat')
    right_eyebrow_height_socket_1.default_value = 0.0
    right_eyebrow_height_socket_1.min_value = -10000.0
    right_eyebrow_height_socket_1.max_value = 10000.0
    right_eyebrow_height_socket_1.subtype = 'NONE'
    right_eyebrow_height_socket_1.attribute_domain = 'POINT'


    #initialize drone_eyes nodes
    #node Group Output
    group_output_3 = drone_eyes.nodes.new("NodeGroupOutput")
    group_output_3.name = "Group Output"
    group_output_3.is_active_output = True

    #node Math.005
    math_005_2 = drone_eyes.nodes.new("ShaderNodeMath")
    math_005_2.name = "Math.005"
    math_005_2.hide = True
    math_005_2.operation = 'MULTIPLY_ADD'
    math_005_2.use_clamp = False
    #Value_001
    math_005_2.inputs[1].default_value = 1.0

    #node Math.007
    math_007_1 = drone_eyes.nodes.new("ShaderNodeMath")
    math_007_1.name = "Math.007"
    math_007_1.hide = True
    math_007_1.operation = 'MULTIPLY_ADD'
    math_007_1.use_clamp = False
    #Value_001
    math_007_1.inputs[1].default_value = 1.0

    #node Math.001
    math_001_2 = drone_eyes.nodes.new("ShaderNodeMath")
    math_001_2.name = "Math.001"
    math_001_2.hide = True
    math_001_2.operation = 'MULTIPLY_ADD'
    math_001_2.use_clamp = False
    #Value_001
    math_001_2.inputs[1].default_value = 1.0

    #node Math.004
    math_004_1 = drone_eyes.nodes.new("ShaderNodeMath")
    math_004_1.name = "Math.004"
    math_004_1.hide = True
    math_004_1.operation = 'MULTIPLY_ADD'
    math_004_1.use_clamp = False
    #Value_001
    math_004_1.inputs[1].default_value = 1.0

    #node Math.003
    math_003_2 = drone_eyes.nodes.new("ShaderNodeMath")
    math_003_2.name = "Math.003"
    math_003_2.hide = True
    math_003_2.operation = 'MULTIPLY_ADD'
    math_003_2.use_clamp = False
    #Value_001
    math_003_2.inputs[1].default_value = 1.0

    #node Math
    math_3 = drone_eyes.nodes.new("ShaderNodeMath")
    math_3.name = "Math"
    math_3.hide = True
    math_3.operation = 'MULTIPLY_ADD'
    math_3.use_clamp = False
    #Value_001
    math_3.inputs[1].default_value = 1.0

    #node Math.002
    math_002_2 = drone_eyes.nodes.new("ShaderNodeMath")
    math_002_2.name = "Math.002"
    math_002_2.hide = True
    math_002_2.operation = 'MULTIPLY_ADD'
    math_002_2.use_clamp = False
    #Value_001
    math_002_2.inputs[1].default_value = 1.0

    #node Math.006
    math_006_2 = drone_eyes.nodes.new("ShaderNodeMath")
    math_006_2.name = "Math.006"
    math_006_2.hide = True
    math_006_2.operation = 'MULTIPLY_ADD'
    math_006_2.use_clamp = False
    #Value_001
    math_006_2.inputs[1].default_value = -1.0

    #node Group Input
    group_input_3 = drone_eyes.nodes.new("NodeGroupInput")
    group_input_3.name = "Group Input"

    #node Group.002
    group_002 = drone_eyes.nodes.new("ShaderNodeGroup")
    group_002.name = "Group.002"
    group_002.node_tree = double_eye__internal_join


    #Set locations
    group_output_3.location = (440.2607116699219, 11.44885540008545)
    math_005_2.location = (-262.9158630371094, -186.31057739257812)
    math_007_1.location = (-265.7557067871094, -117.13028717041016)
    math_001_2.location = (-266.7010803222656, -83.96194458007812)
    math_004_1.location = (-268.16748046875, -52.020198822021484)
    math_003_2.location = (-270.68487548828125, -20.239221572875977)
    math_3.location = (-271.6307067871094, 45.15005111694336)
    math_002_2.location = (-270.6853332519531, 11.981712341308594)
    math_006_2.location = (-265.7552490234375, -151.24661254882812)
    group_input_3.location = (-1023.7621459960938, 280.24169921875)
    group_002.location = (136.2057342529297, 271.3695373535156)

    #Set dimensions
    group_output_3.width, group_output_3.height = 140.0, 100.0
    math_005_2.width, math_005_2.height = 140.0, 100.0
    math_007_1.width, math_007_1.height = 140.0, 100.0
    math_001_2.width, math_001_2.height = 140.0, 100.0
    math_004_1.width, math_004_1.height = 140.0, 100.0
    math_003_2.width, math_003_2.height = 140.0, 100.0
    math_3.width, math_3.height = 140.0, 100.0
    math_002_2.width, math_002_2.height = 140.0, 100.0
    math_006_2.width, math_006_2.height = 140.0, 100.0
    group_input_3.width, group_input_3.height = 158.4017333984375, 100.0
    group_002.width, group_002.height = 237.92071533203125, 100.0

    #initialize drone_eyes links
    #group_002.Value -> group_output_3.Value
    drone_eyes.links.new(group_002.outputs[0], group_output_3.inputs[0])
    #group_input_3.Pupil Size -> group_002.Pupil Size
    drone_eyes.links.new(group_input_3.outputs[0], group_002.inputs[0])
    #group_input_3.Seperation -> group_002.Seperation
    drone_eyes.links.new(group_input_3.outputs[1], group_002.inputs[1])
    #group_input_3.Left Pupil Offset -> group_002.Left Pupil Offset
    drone_eyes.links.new(group_input_3.outputs[4], group_002.inputs[4])
    #group_input_3.Right Pupil Offset -> group_002.Right Pupil Offset
    drone_eyes.links.new(group_input_3.outputs[5], group_002.inputs[5])
    #group_input_3.Left Eye Offset -> group_002.Left Eye Offset
    drone_eyes.links.new(group_input_3.outputs[6], group_002.inputs[6])
    #group_input_3.Right Eye Offset -> group_002.Right Eye Offset
    drone_eyes.links.new(group_input_3.outputs[7], group_002.inputs[7])
    #group_input_3.Eyebrow flatness -> math_3.Value
    drone_eyes.links.new(group_input_3.outputs[8], math_3.inputs[0])
    #group_input_3.Eyebrow Size -> math_002_2.Value
    drone_eyes.links.new(group_input_3.outputs[9], math_002_2.inputs[0])
    #math_002_2.Value -> group_002.Left EyeBrow Size
    drone_eyes.links.new(math_002_2.outputs[0], group_002.inputs[9])
    #math_3.Value -> group_002.Left Eyebrow Flatness
    drone_eyes.links.new(math_3.outputs[0], group_002.inputs[8])
    #group_input_3.Eyebrow angle -> math_003_2.Value
    drone_eyes.links.new(group_input_3.outputs[10], math_003_2.inputs[0])
    #math_004_1.Value -> group_002.left EyeBrow height
    drone_eyes.links.new(math_004_1.outputs[0], group_002.inputs[11])
    #math_003_2.Value -> group_002.Left Eyebrow angle
    drone_eyes.links.new(math_003_2.outputs[0], group_002.inputs[10])
    #group_input_3.EyeBrow height -> math_004_1.Value
    drone_eyes.links.new(group_input_3.outputs[11], math_004_1.inputs[0])
    #math_001_2.Value -> group_002.Right Eyebrow Flatnessa
    drone_eyes.links.new(math_001_2.outputs[0], group_002.inputs[12])
    #math_007_1.Value -> group_002.right EyeBrow Size
    drone_eyes.links.new(math_007_1.outputs[0], group_002.inputs[13])
    #math_005_2.Value -> group_002.Right EyeBrow height
    drone_eyes.links.new(math_005_2.outputs[0], group_002.inputs[15])
    #group_input_3.Eyebrow flatness -> math_001_2.Value
    drone_eyes.links.new(group_input_3.outputs[8], math_001_2.inputs[0])
    #group_input_3.Eyebrow Size -> math_007_1.Value
    drone_eyes.links.new(group_input_3.outputs[9], math_007_1.inputs[0])
    #group_input_3.Eyebrow angle -> math_006_2.Value
    drone_eyes.links.new(group_input_3.outputs[10], math_006_2.inputs[0])
    #group_input_3.EyeBrow height -> math_005_2.Value
    drone_eyes.links.new(group_input_3.outputs[11], math_005_2.inputs[0])
    #math_006_2.Value -> group_002.Right Eyebrow angle
    drone_eyes.links.new(math_006_2.outputs[0], group_002.inputs[14])
    #group_input_3.Left Eyebrow Flatness -> math_3.Value
    drone_eyes.links.new(group_input_3.outputs[12], math_3.inputs[2])
    #group_input_3.Left Eyebrow Size -> math_002_2.Value
    drone_eyes.links.new(group_input_3.outputs[13], math_002_2.inputs[2])
    #group_input_3.Left Eyebrow Angle -> math_003_2.Value
    drone_eyes.links.new(group_input_3.outputs[14], math_003_2.inputs[2])
    #group_input_3.Left Eyebrow Height -> math_004_1.Value
    drone_eyes.links.new(group_input_3.outputs[15], math_004_1.inputs[2])
    #group_input_3.Right Eyebrow Flatness -> math_001_2.Value
    drone_eyes.links.new(group_input_3.outputs[16], math_001_2.inputs[2])
    #group_input_3.Eight Eyebrow Size -> math_007_1.Value
    drone_eyes.links.new(group_input_3.outputs[17], math_007_1.inputs[2])
    #group_input_3.Right Eyebrow Angle -> math_006_2.Value
    drone_eyes.links.new(group_input_3.outputs[18], math_006_2.inputs[2])
    #group_input_3.Right Eyebrow Height -> math_005_2.Value
    drone_eyes.links.new(group_input_3.outputs[19], math_005_2.inputs[2])
    #group_input_3.Eye Offset -> group_002.Pupil Offset
    drone_eyes.links.new(group_input_3.outputs[2], group_002.inputs[3])
    #group_input_3.Pupil Offset -> group_002.Eye Offset
    drone_eyes.links.new(group_input_3.outputs[3], group_002.inputs[2])
    return drone_eyes

drone_eyes = drone_eyes_node_group()

#initialize Eyes node group
def eyes_node_group():

    eyes = mat.node_tree
    #start with a clean node tree
    for node in eyes.nodes:
        eyes.nodes.remove(node)
    eyes.color_tag = 'NONE'
    eyes.description = ""
    eyes.default_group_node_width = 140
    

    #eyes interface

    #initialize eyes nodes
    #node Principled BSDF
    principled_bsdf = eyes.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK_SKIN'
    #Base Color
    principled_bsdf.inputs[0].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
    #Metallic
    principled_bsdf.inputs[1].default_value = 0.0
    #Roughness
    principled_bsdf.inputs[2].default_value = 0.5
    #IOR
    principled_bsdf.inputs[3].default_value = 1.4500000476837158
    #Alpha
    principled_bsdf.inputs[4].default_value = 1.0
    #Normal
    principled_bsdf.inputs[5].default_value = (0.0, 0.0, 0.0)
    #Diffuse Roughness
    principled_bsdf.inputs[7].default_value = 0.0
    #Subsurface Weight
    principled_bsdf.inputs[8].default_value = 0.0
    #Subsurface Radius
    principled_bsdf.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    #Subsurface Scale
    principled_bsdf.inputs[10].default_value = 0.05000000074505806
    #Subsurface IOR
    principled_bsdf.inputs[11].default_value = 1.399999976158142
    #Subsurface Anisotropy
    principled_bsdf.inputs[12].default_value = 0.0
    #Specular IOR Level
    principled_bsdf.inputs[13].default_value = 0.5
    #Specular Tint
    principled_bsdf.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    #Anisotropic
    principled_bsdf.inputs[15].default_value = 0.0
    #Anisotropic Rotation
    principled_bsdf.inputs[16].default_value = 0.0
    #Tangent
    principled_bsdf.inputs[17].default_value = (0.0, 0.0, 0.0)
    #Transmission Weight
    principled_bsdf.inputs[18].default_value = 0.0
    #Coat Weight
    principled_bsdf.inputs[19].default_value = 0.0
    #Coat Roughness
    principled_bsdf.inputs[20].default_value = 0.029999999329447746
    #Coat IOR
    principled_bsdf.inputs[21].default_value = 1.5
    #Coat Tint
    principled_bsdf.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    #Coat Normal
    principled_bsdf.inputs[23].default_value = (0.0, 0.0, 0.0)
    #Sheen Weight
    principled_bsdf.inputs[24].default_value = 0.0
    #Sheen Roughness
    principled_bsdf.inputs[25].default_value = 0.5
    #Sheen Tint
    principled_bsdf.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    #Emission Color
    principled_bsdf.inputs[27].default_value = (0.0, 0.0, 0.0, 1.0)
    #Emission Strength
    principled_bsdf.inputs[28].default_value = 1.0
    #Thin Film Thickness
    principled_bsdf.inputs[29].default_value = 0.0
    #Thin Film IOR
    principled_bsdf.inputs[30].default_value = 1.3300000429153442

    #node Texture Coordinate
    texture_coordinate = eyes.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False

    #node Separate XYZ
    separate_xyz_2 = eyes.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_2.name = "Separate XYZ"

    #node Material Output
    material_output = eyes.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    #Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Thickness
    material_output.inputs[3].default_value = 0.0

    #node Math
    math_4 = eyes.nodes.new("ShaderNodeMath")
    math_4.name = "Math"
    math_4.operation = 'GREATER_THAN'
    math_4.use_clamp = False
    #Value_001
    math_4.inputs[1].default_value = 0.5

    #node Mix Shader
    mix_shader = eyes.nodes.new("ShaderNodeMixShader")
    mix_shader.name = "Mix Shader"

    #node Mix Shader.001
    mix_shader_001 = eyes.nodes.new("ShaderNodeMixShader")
    mix_shader_001.name = "Mix Shader.001"
    #Fac
    mix_shader_001.inputs[0].default_value = 0.5

    #node Transparent BSDF
    transparent_bsdf = eyes.nodes.new("ShaderNodeBsdfTransparent")
    transparent_bsdf.name = "Transparent BSDF"
    #Color
    transparent_bsdf.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)

    #node Emission
    emission = eyes.nodes.new("ShaderNodeEmission")
    emission.name = "Emission"
    #Color
    emission.inputs[0].default_value = (0.06342797726392746, 0.07041695713996887, 1.0, 1.0)
    #Strength
    emission.inputs[1].default_value = 15.600006103515625

    #node Group
    group_2 = eyes.nodes.new("ShaderNodeGroup")
    group_2.name = "Group"
    group_2.node_tree = drone_eyes
    #Input_1
    group_2.inputs[0].default_value = 0.25
    #Input_2
    group_2.inputs[1].default_value = 0.20000000298023224
    #Input_3
    group_2.inputs[2].default_value = (0.0, 0.19999998807907104, 0.0)
    #Input_4
    group_2.inputs[3].default_value = (0.0, 0.09999999403953552, 0.0)
    #Input_6
    group_2.inputs[4].default_value = (0.0, 0.0, 0.0)
    #Input_7
    group_2.inputs[5].default_value = (0.0, 0.0, 0.0)
    #Input_8
    group_2.inputs[6].default_value = (0.0, 0.0, 0.0)
    #Input_9
    group_2.inputs[7].default_value = (0.0, 0.0, 0.0)
    #Input_10
    group_2.inputs[8].default_value = 26.099998474121094
    #Input_11
    group_2.inputs[9].default_value = 0.10000000149011612
    #Input_12
    group_2.inputs[10].default_value = 0.07504915446043015
    #Input_13
    group_2.inputs[11].default_value = -0.03999999910593033
    #Input_15
    group_2.inputs[12].default_value = 0.0
    #Input_16
    group_2.inputs[13].default_value = 0.0
    #Input_17
    group_2.inputs[14].default_value = 0.0
    #Input_18
    group_2.inputs[15].default_value = 0.0
    #Input_19
    group_2.inputs[16].default_value = 0.0
    #Input_20
    group_2.inputs[17].default_value = 0.0
    #Input_21
    group_2.inputs[18].default_value = 0.0
    #Input_22
    group_2.inputs[19].default_value = 0.0

    #node Mix Shader.002
    mix_shader_002 = eyes.nodes.new("ShaderNodeMixShader")
    mix_shader_002.name = "Mix Shader.002"
    #Fac
    mix_shader_002.inputs[0].default_value = 0.0


    #Set locations
    principled_bsdf.location = (10.0, 300.0)
    texture_coordinate.location = (277.49188232421875, -140.7943115234375)
    separate_xyz_2.location = (797.1177368164062, 4.6732025146484375)
    material_output.location = (1683.073486328125, -71.07340240478516)
    math_4.location = (1007.4834594726562, 34.96172332763672)
    mix_shader.location = (1044.779052734375, -212.3124542236328)
    mix_shader_001.location = (824.7791137695312, -286.4544982910156)
    transparent_bsdf.location = (707.2386474609375, -140.78436279296875)
    emission.location = (647.8858642578125, -423.52587890625)
    group_2.location = (238.4918975830078, -425.77630615234375)
    mix_shader_002.location = (1306.969970703125, -163.29971313476562)

    #Set dimensions
    principled_bsdf.width, principled_bsdf.height = 240.0, 100.0
    texture_coordinate.width, texture_coordinate.height = 140.0, 100.0
    separate_xyz_2.width, separate_xyz_2.height = 140.0, 100.0
    material_output.width, material_output.height = 140.0, 100.0
    math_4.width, math_4.height = 140.0, 100.0
    mix_shader.width, mix_shader.height = 140.0, 100.0
    mix_shader_001.width, mix_shader_001.height = 140.0, 100.0
    transparent_bsdf.width, transparent_bsdf.height = 140.0, 100.0
    emission.width, emission.height = 140.0, 100.0
    group_2.width, group_2.height = 251.4217529296875, 100.0
    mix_shader_002.width, mix_shader_002.height = 140.0, 100.0

    #initialize eyes links
    #group_2.Value -> mix_shader.Fac
    eyes.links.new(group_2.outputs[0], mix_shader.inputs[0])
    #texture_coordinate.Normal -> separate_xyz_2.Vector
    eyes.links.new(texture_coordinate.outputs[1], separate_xyz_2.inputs[0])
    #separate_xyz_2.Z -> math_4.Value
    eyes.links.new(separate_xyz_2.outputs[2], math_4.inputs[0])
    #mix_shader_002.Shader -> material_output.Surface
    eyes.links.new(mix_shader_002.outputs[0], material_output.inputs[0])
    #emission.Emission -> mix_shader_001.Shader
    eyes.links.new(emission.outputs[0], mix_shader_001.inputs[1])
    #mix_shader_001.Shader -> mix_shader.Shader
    eyes.links.new(mix_shader_001.outputs[0], mix_shader.inputs[2])
    #transparent_bsdf.BSDF -> mix_shader.Shader
    eyes.links.new(transparent_bsdf.outputs[0], mix_shader.inputs[1])
    #transparent_bsdf.BSDF -> mix_shader_002.Shader
    eyes.links.new(transparent_bsdf.outputs[0], mix_shader_002.inputs[1])
    #mix_shader.Shader -> mix_shader_002.Shader
    eyes.links.new(mix_shader.outputs[0], mix_shader_002.inputs[2])
    return eyes

eyes = eyes_node_group()



from labelbox.data.serialization.ndjson.converter import NDJsonConverter


data = [{'uuid': 'b862c586-8614-483c-b5e6-82810f70cac0', 'schemaId': 'ckrazcueb16og0z6609jj7y3y', 'dataRow': {'id': 'ckrazctum0z8a0ybc0b0o0g0v'}, 'bbox': {'top': 1352, 'left': 2275, 'height': 350, 'width': 139}}, {'uuid': '751fc725-f7b6-48ed-89b0-dd7d94d08af6', 'schemaId': 'ckrazcuec16ok0z66f956apb7', 'dataRow': {'id': 'ckrazctum0z8a0ybc0b0o0g0v'}, 'mask': {'instanceURI': 'https://storage.labelbox.com/ckqcx1czn06830y61gh9v02cs%2F3e729327-f038-f66c-186e-45e921ef9717-1?Expires=1626806874672&KeyName=labelbox-assets-key-3&Signature=YsUOGKrsqmAZ68vT9BlPJOaRyLY', 'colorRGB': (255, 0, 0)}}, {'uuid': '43d719ac-5d7f-4aea-be00-2ebfca0900fd', 'schemaId': 'ckrazcuec16oi0z66dzrd8pfl', 'dataRow': {'id': 'ckrazctum0z8a0ybc0b0o0g0v'}, 'polygon': [{'x': 1118, 'y': 935}, {'x': 1117, 'y': 935}, {'x': 1116, 'y': 935}, {'x': 1115, 'y': 935}, {'x': 1114, 'y': 935}, {'x': 1113, 'y': 935}, {'x': 1112, 'y': 935}, {'x': 1111, 'y': 935}, {'x': 1110, 'y': 935}, {'x': 1109, 'y': 935}, {'x': 1108, 'y': 935}, {'x': 1108, 'y': 934}, {'x': 1107, 'y': 934}, {'x': 1106, 'y': 934}, {'x': 1105, 'y': 934}, {'x': 1105, 'y': 933}, {'x': 1104, 'y': 933}, {'x': 1103, 'y': 933}, {'x': 1103, 'y': 932}, {'x': 1102, 'y': 932}, {'x': 1101, 'y': 932}, {'x': 1100, 'y': 932}, {'x': 1099, 'y': 932}, {'x': 1098, 'y': 932}, {'x': 1097, 'y': 932}, {'x': 1097, 'y': 931}, {'x': 1096, 'y': 931}, {'x': 1095, 'y': 931}, {'x': 1094, 'y': 931}, {'x': 1093, 'y': 931}, {'x': 1092, 'y': 931}, {'x': 1091, 'y': 931}, {'x': 1090, 'y': 931}, {'x': 1090, 'y': 930}, {'x': 1089, 'y': 930}, {'x': 1088, 'y': 930}, {'x': 1087, 'y': 930}, {'x': 1087, 'y': 929}, {'x': 1086, 'y': 929}, {'x': 1085, 'y': 929}, {'x': 1084, 'y': 929}, {'x': 1084, 'y': 928}, {'x': 1083, 'y': 928}, {'x': 1083, 'y': 927}, {'x': 1082, 'y': 927}, {'x': 1081, 'y': 927}, {'x': 1081, 'y': 926}, {'x': 1080, 'y': 926}, {'x': 1080, 'y': 925}, {'x': 1079, 'y': 925}, {'x': 1078, 'y': 925}, {'x': 1078, 'y': 924}, {'x': 1077, 'y': 924}, {'x': 1076, 'y': 924}, {'x': 1076, 'y': 923}, {'x': 1075, 'y': 923}, {'x': 1074, 'y': 923}, {'x': 1073, 'y': 923}, {'x': 1073, 'y': 922}, {'x': 1072, 'y': 922}, {'x': 1071, 'y': 922}, {'x': 1070, 'y': 922}, {'x': 1070, 'y': 921}, {'x': 1069, 'y': 921}, {'x': 1068, 'y': 921}, {'x': 1067, 'y': 921}, {'x': 1066, 'y': 921}, {'x': 1065, 'y': 921}, {'x': 1064, 'y': 921}, {'x': 1063, 'y': 921}, {'x': 1062, 'y': 921}, {'x': 1061, 'y': 921}, {'x': 1060, 'y': 921}, {'x': 1059, 'y': 921}, {'x': 1058, 'y': 921}, {'x': 1058, 'y': 920}, {'x': 1057, 'y': 920}, {'x': 1057, 'y': 919}, {'x': 1056, 'y': 919}, {'x': 1057, 'y': 918}, {'x': 1057, 'y': 918}, {'x': 1057, 'y': 917}, {'x': 1058, 'y': 916}, {'x': 1058, 'y': 916}, {'x': 1059, 'y': 915}, {'x': 1059, 'y': 915}, {'x': 1060, 'y': 914}, {'x': 1060, 'y': 914}, {'x': 1061, 'y': 913}, {'x': 1061, 'y': 913}, {'x': 1062, 'y': 912}, {'x': 1063, 'y': 912}, {'x': 1063, 'y': 912}, {'x': 1064, 'y': 911}, {'x': 1064, 'y': 911}, {'x': 1065, 'y': 910}, {'x': 1066, 'y': 910}, {'x': 1066, 'y': 910}, {'x': 1067, 'y': 909}, {'x': 1068, 'y': 909}, {'x': 1068, 'y': 909}, {'x': 1069, 'y': 908}, {'x': 1070, 'y': 908}, {'x': 1071, 'y': 908}, {'x': 1072, 'y': 908}, {'x': 1072, 'y': 908}, {'x': 1073, 'y': 907}, {'x': 1074, 'y': 907}, {'x': 1075, 'y': 907}, {'x': 1076, 'y': 907}, {'x': 1077, 'y': 907}, {'x': 1078, 'y': 907}, {'x': 1079, 'y': 907}, {'x': 1080, 'y': 907}, {'x': 1081, 'y': 907}, {'x': 1082, 'y': 907}, {'x': 1083, 'y': 907}, {'x': 1084, 'y': 907}, {'x': 1085, 'y': 907}, {'x': 1086, 'y': 907}, {'x': 1087, 'y': 907}, {'x': 1088, 'y': 907}, {'x': 1089, 'y': 907}, {'x': 1090, 'y': 907}, {'x': 1091, 'y': 907}, {'x': 1091, 'y': 908}, {'x': 1092, 'y': 908}, {'x': 1093, 'y': 908}, {'x': 1094, 'y': 908}, {'x': 1095, 'y': 908}, {'x': 1095, 'y': 909}, {'x': 1096, 'y': 909}, {'x': 1097, 'y': 909}, {'x': 1097, 'y': 910}, {'x': 1098, 'y': 910}, {'x': 1099, 'y': 910}, {'x': 1099, 'y': 911}, {'x': 1100, 'y': 911}, {'x': 1101, 'y': 911}, {'x': 1101, 'y': 912}, {'x': 1102, 'y': 912}, {'x': 1103, 'y': 912}, {'x': 1103, 'y': 913}, {'x': 1104, 'y': 913}, {'x': 1104, 'y': 914}, {'x': 1105, 'y': 914}, {'x': 1105, 'y': 915}, {'x': 1106, 'y': 915}, {'x': 1107, 'y': 915}, {'x': 1107, 'y': 916}, {'x': 1108, 'y': 916}, {'x': 1108, 'y': 917}, {'x': 1109, 'y': 917}, {'x': 1109, 'y': 918}, {'x': 1110, 'y': 918}, {'x': 1110, 'y': 919}, {'x': 1111, 'y': 919}, {'x': 1111, 'y': 920}, {'x': 1112, 'y': 920}, {'x': 1112, 'y': 921}, {'x': 1113, 'y': 921}, {'x': 1113, 'y': 922}, {'x': 1114, 'y': 922}, {'x': 1114, 'y': 923}, {'x': 1115, 'y': 923}, {'x': 1115, 'y': 924}, {'x': 1115, 'y': 925}, {'x': 1116, 'y': 925}, {'x': 1116, 'y': 926}, {'x': 1117, 'y': 926}, {'x': 1117, 'y': 927}, {'x': 1117, 'y': 928}, {'x': 1118, 'y': 928}, {'x': 1118, 'y': 929}, {'x': 1119, 'y': 929}, {'x': 1119, 'y': 930}, {'x': 1120, 'y': 930}, {'x': 1120, 'y': 931}, {'x': 1120, 'y': 932}, {'x': 1120, 'y': 932}, {'x': 1119, 'y': 933}, {'x': 1119, 'y': 934}, {'x': 1119, 'y': 934}, {'x': 1118, 'y': 935}, {'x': 1118, 'y': 935}]}, {'uuid': 'b98f3a45-3328-41a0-9077-373a8177ebf2', 'schemaId': 'ckrazcuec16om0z66bhhh4tp7', 'dataRow': {'id': 'ckrazctum0z8a0ybc0b0o0g0v'}, 'point': {'x': 2122, 'y': 1457}}]




def test_nested():
    res = NDJsonConverter.deserialize(data)
    res.data = list(res.data)
    res = list(NDJsonConverter.serialize(res))
    for r in res:
        r.pop('classifications', None)
    assert res == data


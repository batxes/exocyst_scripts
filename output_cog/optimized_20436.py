import _surface
import chimera
try:
  import chimera.runCommand
except:
  pass
from VolumePath import markerset as ms
try:
  from VolumePath import Marker_Set, Link
  new_marker_set=Marker_Set
except:
  from VolumePath import volume_path_dialog
  d= volume_path_dialog(True)
  new_marker_set= d.new_marker_set
marker_sets={}
surf_sets={}
if "Cog2_GFPN" not in marker_sets:
  s=new_marker_set('Cog2_GFPN')
  marker_sets["Cog2_GFPN"]=s
s= marker_sets["Cog2_GFPN"]
mark=s.place_marker((349.302, 442.979, 491.344), (0.89, 0.1, 0.1), 18.4716)
if "Cog2_0" not in marker_sets:
  s=new_marker_set('Cog2_0')
  marker_sets["Cog2_0"]=s
s= marker_sets["Cog2_0"]
mark=s.place_marker((414.852, 458.31, 476.575), (0.89, 0.1, 0.1), 17.1475)
if "Cog2_1" not in marker_sets:
  s=new_marker_set('Cog2_1')
  marker_sets["Cog2_1"]=s
s= marker_sets["Cog2_1"]
mark=s.place_marker((495.757, 468.556, 463.449), (0.89, 0.1, 0.1), 17.1475)
if "Cog2_GFPC" not in marker_sets:
  s=new_marker_set('Cog2_GFPC')
  marker_sets["Cog2_GFPC"]=s
s= marker_sets["Cog2_GFPC"]
mark=s.place_marker((445.846, 346.316, 507.684), (0.89, 0.1, 0.1), 18.4716)
if "Cog2_Anch" not in marker_sets:
  s=new_marker_set('Cog2_Anch')
  marker_sets["Cog2_Anch"]=s
s= marker_sets["Cog2_Anch"]
mark=s.place_marker((672.444, 537.912, 427.002), (0.89, 0.1, 0.1), 18.4716)
if "Cog3_GFPN" not in marker_sets:
  s=new_marker_set('Cog3_GFPN')
  marker_sets["Cog3_GFPN"]=s
s= marker_sets["Cog3_GFPN"]
mark=s.place_marker((393.594, 456.745, 491.247), (1, 1, 0), 18.4716)
if "Cog3_0" not in marker_sets:
  s=new_marker_set('Cog3_0')
  marker_sets["Cog3_0"]=s
s= marker_sets["Cog3_0"]
mark=s.place_marker((392.814, 456.724, 491.901), (1, 1, 0.2), 17.1475)
if "Cog3_1" not in marker_sets:
  s=new_marker_set('Cog3_1')
  marker_sets["Cog3_1"]=s
s= marker_sets["Cog3_1"]
mark=s.place_marker((403.834, 470.942, 513.265), (1, 1, 0.2), 17.1475)
if "Cog3_2" not in marker_sets:
  s=new_marker_set('Cog3_2')
  marker_sets["Cog3_2"]=s
s= marker_sets["Cog3_2"]
mark=s.place_marker((425.547, 470.346, 530.768), (1, 1, 0.2), 17.1475)
if "Cog3_3" not in marker_sets:
  s=new_marker_set('Cog3_3')
  marker_sets["Cog3_3"]=s
s= marker_sets["Cog3_3"]
mark=s.place_marker((430.668, 489.097, 551.039), (1, 1, 0.2), 17.1475)
if "Cog3_4" not in marker_sets:
  s=new_marker_set('Cog3_4')
  marker_sets["Cog3_4"]=s
s= marker_sets["Cog3_4"]
mark=s.place_marker((413.722, 481.095, 571.876), (1, 1, 0.2), 17.1475)
if "Cog3_5" not in marker_sets:
  s=new_marker_set('Cog3_5')
  marker_sets["Cog3_5"]=s
s= marker_sets["Cog3_5"]
mark=s.place_marker((389.729, 472.751, 583.309), (1, 1, 0.2), 17.1475)
if "Cog3_GFPC" not in marker_sets:
  s=new_marker_set('Cog3_GFPC')
  marker_sets["Cog3_GFPC"]=s
s= marker_sets["Cog3_GFPC"]
mark=s.place_marker((367.749, 458.317, 479.312), (1, 1, 0.4), 18.4716)
if "Cog3_Anch" not in marker_sets:
  s=new_marker_set('Cog3_Anch')
  marker_sets["Cog3_Anch"]=s
s= marker_sets["Cog3_Anch"]
mark=s.place_marker((412.226, 494.859, 684.588), (1, 1, 0.4), 18.4716)
if "Cog4_GFPN" not in marker_sets:
  s=new_marker_set('Cog4_GFPN')
  marker_sets["Cog4_GFPN"]=s
s= marker_sets["Cog4_GFPN"]
mark=s.place_marker((575.18, 558.918, 583.617), (0, 0, 0.8), 18.4716)
if "Cog4_0" not in marker_sets:
  s=new_marker_set('Cog4_0')
  marker_sets["Cog4_0"]=s
s= marker_sets["Cog4_0"]
mark=s.place_marker((575.18, 558.918, 583.617), (0, 0, 0.8), 17.1475)
if "Cog4_1" not in marker_sets:
  s=new_marker_set('Cog4_1')
  marker_sets["Cog4_1"]=s
s= marker_sets["Cog4_1"]
mark=s.place_marker((566.077, 548.565, 557.325), (0, 0, 0.8), 17.1475)
if "Cog4_2" not in marker_sets:
  s=new_marker_set('Cog4_2')
  marker_sets["Cog4_2"]=s
s= marker_sets["Cog4_2"]
mark=s.place_marker((553.893, 537.384, 532.818), (0, 0, 0.8), 17.1475)
if "Cog4_3" not in marker_sets:
  s=new_marker_set('Cog4_3')
  marker_sets["Cog4_3"]=s
s= marker_sets["Cog4_3"]
mark=s.place_marker((534.494, 524.961, 514.5), (0, 0, 0.8), 17.1475)
if "Cog4_4" not in marker_sets:
  s=new_marker_set('Cog4_4')
  marker_sets["Cog4_4"]=s
s= marker_sets["Cog4_4"]
mark=s.place_marker((508.235, 515.088, 506.4), (0, 0, 0.8), 17.1475)
if "Cog4_5" not in marker_sets:
  s=new_marker_set('Cog4_5')
  marker_sets["Cog4_5"]=s
s= marker_sets["Cog4_5"]
mark=s.place_marker((480.234, 506.629, 503.025), (0, 0, 0.8), 17.1475)
if "Cog4_6" not in marker_sets:
  s=new_marker_set('Cog4_6')
  marker_sets["Cog4_6"]=s
s= marker_sets["Cog4_6"]
mark=s.place_marker((451.559, 501.305, 499.39), (0, 0, 0.8), 17.1475)
if "Cog4_GFPC" not in marker_sets:
  s=new_marker_set('Cog4_GFPC')
  marker_sets["Cog4_GFPC"]=s
s= marker_sets["Cog4_GFPC"]
mark=s.place_marker((564.13, 507.184, 730.689), (0, 0, 0.8), 18.4716)
if "Cog4_Anch" not in marker_sets:
  s=new_marker_set('Cog4_Anch')
  marker_sets["Cog4_Anch"]=s
s= marker_sets["Cog4_Anch"]
mark=s.place_marker((317.654, 484.108, 275.857), (0, 0, 0.8), 18.4716)
if "Cog5_GFPN" not in marker_sets:
  s=new_marker_set('Cog5_GFPN')
  marker_sets["Cog5_GFPN"]=s
s= marker_sets["Cog5_GFPN"]
mark=s.place_marker((468.75, 509.728, 470.442), (0.3, 0.3, 0.3), 18.4716)
if "Cog5_0" not in marker_sets:
  s=new_marker_set('Cog5_0')
  marker_sets["Cog5_0"]=s
s= marker_sets["Cog5_0"]
mark=s.place_marker((468.75, 509.728, 470.442), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_1" not in marker_sets:
  s=new_marker_set('Cog5_1')
  marker_sets["Cog5_1"]=s
s= marker_sets["Cog5_1"]
mark=s.place_marker((470.178, 482.458, 478.664), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_2" not in marker_sets:
  s=new_marker_set('Cog5_2')
  marker_sets["Cog5_2"]=s
s= marker_sets["Cog5_2"]
mark=s.place_marker((472.827, 454.174, 482.668), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_3" not in marker_sets:
  s=new_marker_set('Cog5_3')
  marker_sets["Cog5_3"]=s
s= marker_sets["Cog5_3"]
mark=s.place_marker((489.444, 435.548, 468.621), (0.3, 0.3, 0.3), 17.1475)
if "Cog5_GFPC" not in marker_sets:
  s=new_marker_set('Cog5_GFPC')
  marker_sets["Cog5_GFPC"]=s
s= marker_sets["Cog5_GFPC"]
mark=s.place_marker((373.603, 391.402, 478.716), (0.3, 0.3, 0.3), 18.4716)
if "Cog5_Anch" not in marker_sets:
  s=new_marker_set('Cog5_Anch')
  marker_sets["Cog5_Anch"]=s
s= marker_sets["Cog5_Anch"]
mark=s.place_marker((606.894, 477.181, 454.79), (0.3, 0.3, 0.3), 18.4716)
if "Cog6_GFPN" not in marker_sets:
  s=new_marker_set('Cog6_GFPN')
  marker_sets["Cog6_GFPN"]=s
s= marker_sets["Cog6_GFPN"]
mark=s.place_marker((408.594, 431.903, 477.576), (0.21, 0.49, 0.72), 18.4716)
if "Cog6_0" not in marker_sets:
  s=new_marker_set('Cog6_0')
  marker_sets["Cog6_0"]=s
s= marker_sets["Cog6_0"]
mark=s.place_marker((408.507, 431.16, 477.421), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_1" not in marker_sets:
  s=new_marker_set('Cog6_1')
  marker_sets["Cog6_1"]=s
s= marker_sets["Cog6_1"]
mark=s.place_marker((388.239, 416.617, 464.626), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_2" not in marker_sets:
  s=new_marker_set('Cog6_2')
  marker_sets["Cog6_2"]=s
s= marker_sets["Cog6_2"]
mark=s.place_marker((371.137, 427.955, 483.949), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_3" not in marker_sets:
  s=new_marker_set('Cog6_3')
  marker_sets["Cog6_3"]=s
s= marker_sets["Cog6_3"]
mark=s.place_marker((363.552, 445.842, 504.634), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_4" not in marker_sets:
  s=new_marker_set('Cog6_4')
  marker_sets["Cog6_4"]=s
s= marker_sets["Cog6_4"]
mark=s.place_marker((370.148, 469.937, 518.556), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_5" not in marker_sets:
  s=new_marker_set('Cog6_5')
  marker_sets["Cog6_5"]=s
s= marker_sets["Cog6_5"]
mark=s.place_marker((375.856, 483.832, 543.268), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_6" not in marker_sets:
  s=new_marker_set('Cog6_6')
  marker_sets["Cog6_6"]=s
s= marker_sets["Cog6_6"]
mark=s.place_marker((382.171, 499.957, 566.291), (0.21, 0.49, 0.72), 17.1475)
if "Cog6_GFPC" not in marker_sets:
  s=new_marker_set('Cog6_GFPC')
  marker_sets["Cog6_GFPC"]=s
s= marker_sets["Cog6_GFPC"]
mark=s.place_marker((394.148, 531.147, 488.18), (0.21, 0.49, 0.72), 18.4716)
if "Cog6_Anch" not in marker_sets:
  s=new_marker_set('Cog6_Anch')
  marker_sets["Cog6_Anch"]=s
s= marker_sets["Cog6_Anch"]
mark=s.place_marker((373.355, 467.881, 647.977), (0.21, 0.49, 0.72), 18.4716)
if "Cog7_GFPN" not in marker_sets:
  s=new_marker_set('Cog7_GFPN')
  marker_sets["Cog7_GFPN"]=s
s= marker_sets["Cog7_GFPN"]
mark=s.place_marker((409.219, 514.922, 447.659), (0.7, 0.7, 0.7), 18.4716)
if "Cog7_0" not in marker_sets:
  s=new_marker_set('Cog7_0')
  marker_sets["Cog7_0"]=s
s= marker_sets["Cog7_0"]
mark=s.place_marker((420.441, 493.448, 449.254), (0.7, 0.7, 0.7), 17.1475)
if "Cog7_1" not in marker_sets:
  s=new_marker_set('Cog7_1')
  marker_sets["Cog7_1"]=s
s= marker_sets["Cog7_1"]
mark=s.place_marker((449.856, 444.083, 459.708), (0.7, 0.7, 0.7), 17.1475)
if "Cog7_2" not in marker_sets:
  s=new_marker_set('Cog7_2')
  marker_sets["Cog7_2"]=s
s= marker_sets["Cog7_2"]
mark=s.place_marker((479.907, 395.191, 470.746), (0.7, 0.7, 0.7), 17.1475)
if "Cog7_GFPC" not in marker_sets:
  s=new_marker_set('Cog7_GFPC')
  marker_sets["Cog7_GFPC"]=s
s= marker_sets["Cog7_GFPC"]
mark=s.place_marker((414.247, 360.808, 439.374), (0.7, 0.7, 0.7), 18.4716)
if "Cog7_Anch" not in marker_sets:
  s=new_marker_set('Cog7_Anch')
  marker_sets["Cog7_Anch"]=s
s= marker_sets["Cog7_Anch"]
mark=s.place_marker((569.393, 355.034, 508.447), (0.7, 0.7, 0.7), 18.4716)
if "Cog8_0" not in marker_sets:
  s=new_marker_set('Cog8_0')
  marker_sets["Cog8_0"]=s
s= marker_sets["Cog8_0"]
mark=s.place_marker((384.465, 490.599, 493.438), (1, 0.5, 0), 17.1475)
if "Cog8_1" not in marker_sets:
  s=new_marker_set('Cog8_1')
  marker_sets["Cog8_1"]=s
s= marker_sets["Cog8_1"]
mark=s.place_marker((411.257, 492.273, 483.958), (1, 0.5, 0), 17.1475)
if "Cog8_2" not in marker_sets:
  s=new_marker_set('Cog8_2')
  marker_sets["Cog8_2"]=s
s= marker_sets["Cog8_2"]
mark=s.place_marker((436.933, 483.012, 475.263), (1, 0.5, 0), 17.1475)
if "Cog8_3" not in marker_sets:
  s=new_marker_set('Cog8_3')
  marker_sets["Cog8_3"]=s
s= marker_sets["Cog8_3"]
mark=s.place_marker((450.681, 477.019, 450.628), (1, 0.5, 0), 17.1475)
if "Cog8_4" not in marker_sets:
  s=new_marker_set('Cog8_4')
  marker_sets["Cog8_4"]=s
s= marker_sets["Cog8_4"]
mark=s.place_marker((471.019, 471.03, 431.2), (1, 0.5, 0), 17.1475)
if "Cog8_5" not in marker_sets:
  s=new_marker_set('Cog8_5')
  marker_sets["Cog8_5"]=s
s= marker_sets["Cog8_5"]
mark=s.place_marker((494.576, 467.438, 414.904), (1, 0.5, 0), 17.1475)
if "Cog8_GFPC" not in marker_sets:
  s=new_marker_set('Cog8_GFPC')
  marker_sets["Cog8_GFPC"]=s
s= marker_sets["Cog8_GFPC"]
mark=s.place_marker((422.422, 466.336, 450.295), (1, 0.6, 0.1), 18.4716)
if "Cog8_Anch" not in marker_sets:
  s=new_marker_set('Cog8_Anch')
  marker_sets["Cog8_Anch"]=s
s= marker_sets["Cog8_Anch"]
mark=s.place_marker((568.084, 468.35, 377.92), (1, 0.6, 0.1), 18.4716)
for k in surf_sets.keys():
  chimera.openModels.add([surf_sets[k]])

from graphviz import Digraph

# Create a new directed graph
dot = Digraph("Fall_Detection_Model_Detailed", format="png")

# Define nodes for each detailed component
# Input and Preprocessing
dot.node("Input", "Input\nVideo/Camera Feed")
dot.node("Source", "get_source\nCapture Video/Load Dataset")
dot.node("Resize", "resize\nAdjust Frame Size")

# Pose Estimation and Keypoint Extraction
dot.node("Keypoints", "extract_keypoints_parallel\nExtract Keypoints from Frame")
dot.node("Processor", "Processor\nProcess Frame for Keypoints & Bounding Boxes")

# Feature Extraction
dot.node("Features", "get_all_features\nExtract Bounding Box & Keypoint Features")
dot.node("Height", "get_height_bbox\nCalculate Bounding Box Height")
dot.node("Ratio", "get_ratio_bbox\nCalculate Width-to-Height Ratio")
dot.node("Angle", "get_angle_vertical\nCalculate Keypoint Angle")
dot.node("FrameFeatures", "get_frame_features\nAggregate Features for LSTM")

# LSTM Model for Fall Detection
dot.node("LSTM", "LSTMModel\nTemporal Analysis for Fall Detection")
dot.node("Algorithm", "alg2_sequential\nPredict Fall Events with LSTM Output")

# Alert System
dot.node("Alert", "send_alert_message\nSend Fall Alert to Server")
dot.node("Record", "Record Event\nSave Video & Metadata")

# Define edges for data flow in detail
# Input and Preprocessing flow
dot.edge("Input", "Source")
dot.edge("Source", "Resize")
dot.edge("Resize", "Keypoints")

# Pose Estimation and Keypoint Extraction flow
dot.edge("Keypoints", "Processor")

# Feature Extraction flow
dot.edge("Processor", "Features")
dot.edge("Features", "Height")
dot.edge("Features", "Ratio")
dot.edge("Features", "Angle")
dot.edge("Features", "FrameFeatures")

# LSTM Model flow
dot.edge("FrameFeatures", "LSTM")
dot.edge("LSTM", "Algorithm")

# Alert System flow
dot.edge("Algorithm", "Alert")
dot.edge("Alert", "Record")

# Render and save the graph
dot.render("Fall_Detection_Model_Detailed", view=True)

from bs4 import BeautifulSoup
import csv
import os
import errno
import pathlib

outfile = open('merkandi_website.csv', 'a+', newline='')

writer = csv.writer(outfile)
writer.writerow(
    ["id", "website"])
categories = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9988, 9985, 9984, 9983, 9982, 9981, 9980,
              9979, 9978, 9977, 9976, 9975, 9961, 9960, 9960, 9959, 9958, 9956, 9955, 9954, 9953, 9952, 9950, 9949,
              9948, 9947, 9946, 9945, 9944, 9943, 9942, 9941, 9940, 994, 9937, 9935, 9934, 9933, 9932, 9931, 9930, 9929,
              9928, 9927, 9926, 9925, 9924, 9923, 9922, 9921, 9920, 9918, 9917, 9916, 9914, 9913, 9912, 9911, 9910,
              9910, 9908, 9907, 9906, 9905, 9904, 9903, 9902, 9901, 9898, 9897, 9896, 9894, 9893, 9892, 9891, 9890,
              9889, 9888, 9887, 9886, 9885, 9884, 9882, 9881, 9879, 9879, 9878, 9873, 9872, 9872, 9871, 9870, 9870,
              9869, 9866, 9865, 9863, 9861, 9860, 9859, 9858, 9857, 9856, 9854, 9854, 9853, 9852, 9851, 9850, 9849,
              9847, 9846, 9845, 9844, 9843, 9841, 9840, 9839, 9838, 9837, 9837, 9836, 9835, 9834, 9833, 9832, 9830,
              9829, 9828, 9827, 9826, 9824, 9822, 9820, 9818, 9817, 9815, 9814, 9813, 9812, 9810, 9809, 9808, 9807,
              9806, 9805, 9804, 9803, 9803, 9801, 9800, 9799, 9799, 9798, 9797, 9796, 9795, 9795, 9794, 9793, 9792,
              9791, 9788, 9788, 9786, 9785, 9784, 9782, 9781, 9780, 9779, 9778, 9777, 9776, 9775, 9774, 9773, 9771,
              9770, 9769, 9768, 9767, 9766, 9765, 9764, 9763, 9762, 9761, 9759, 9758, 9756, 9754, 9753, 9751, 9750,
              9749, 9748, 9747, 9746, 9745, 9743, 9742, 9740, 9739, 9738, 9737, 9736, 9735, 9734, 9733, 9732, 9730,
              9728, 9726, 9725, 9724, 9723, 9721, 9720, 9719, 9718, 9717, 9716, 9715, 9714, 9713, 9712, 9712, 9711,
              9710, 9709, 9708, 9707, 9707, 9706, 9706, 9703, 9702, 9701, 9700, 9697, 9696, 9695, 9694, 9693, 9691,
              9690, 9689, 9689, 9688, 9688, 9687, 9687, 9686, 9683, 9682, 9681, 9680, 9679, 9677, 9676, 9675, 9675,
              9674, 9673, 9673, 9672, 9669, 9668, 9666, 9663, 9662, 9661, 9660, 9660, 9659, 9657, 9656, 9655, 9654,
              9652, 9650, 9648, 9648, 9646, 9644, 9643, 9642, 9641, 9640, 9638, 9637, 9636, 9635, 9634, 9632, 9630,
              9629, 9628, 9626, 9625, 9624, 9622, 9621, 9619, 9618, 9617, 9616, 9615, 9614, 9613, 9613, 9612, 9611,
              9610, 9609, 9608, 9607, 9606, 9603, 9602, 9600, 9599, 9598, 9596, 9595, 9593, 9592, 9590, 9589, 9588,
              9587, 9586, 9585, 9584, 9583, 9582, 9581, 9580, 9578, 9576, 9575, 9574, 9573, 9572, 9571, 9569, 9567,
              9566, 9565, 9564, 9563, 9562, 9561, 9558, 9557, 9556, 9554, 9552, 9551, 9548, 9547, 9544, 9541, 9540,
              9539, 9537, 9535, 9535, 9534, 9533, 9532, 9531, 9529, 9528, 9527, 9526, 9524, 9523, 9522, 9521, 9520,
              9518, 9517, 9516, 9515, 9514, 9512, 9511, 9510, 9509, 9508, 9507, 9506, 9505, 9503, 9502, 9501, 9500,
              9499, 9498, 9496, 9494, 9493, 9492, 9491, 9489, 9484, 9482, 9481, 9480, 9479, 9478, 9477, 9475, 9474,
              9473, 9472, 9471, 9470, 9468, 9465, 9464, 9463, 9462, 9461, 9460, 9459, 9457, 9456, 9455, 9454, 9453,
              9452, 9451, 9450, 9449, 9448, 9447, 9445, 9444, 9443, 9443, 9442, 9441, 9440, 9439, 9438, 9437, 9436,
              9434, 9433, 9432, 9431, 9431, 9430, 9429, 9428, 9427, 9426, 9424, 9423, 9422, 9421, 9420, 9419, 9418,
              9417, 9416, 9415, 9414, 9413, 9412, 9410, 9407, 9406, 9405, 9403, 9401, 9399, 9398, 9397, 9396, 9395,
              9394, 9393, 9393, 9392, 9392, 9391, 9390, 9389, 9388, 9386, 9385, 9384, 9383, 9381, 9379, 9378, 9375,
              9374, 9373, 9372, 9371, 9370, 9369, 9367, 9366, 9364, 9363, 9362, 9360, 9358, 9357, 9355, 9354, 9353,
              9353, 9352, 9351, 9350, 9349, 9348, 9347, 9345, 9344, 9342, 9341, 9339, 9338, 9336, 9335, 9334, 9333,
              9330, 9329, 9327, 9326, 9326, 9325, 9323, 9322, 9321, 9320, 9319, 9317, 9316, 9315, 9314, 9313, 9313,
              9312, 9311, 9310, 9309, 9307, 9306, 9305, 9304, 9304, 9302, 9302, 9301, 9298, 9297, 9296, 9295, 9293,
              9292, 9290, 9289, 9287, 9286, 9285, 9284, 9283, 9282, 9282, 9280, 9279, 9275, 9274, 9272, 9271, 9270,
              9269, 9268, 9266, 9265, 9264, 9262, 9261, 9258, 9257, 9253, 9252, 9251, 9250, 9249, 9248, 9245, 9245,
              9243, 9242, 9241, 9238, 9237, 9236, 9235, 9234, 9233, 9232, 9230, 9229, 9223, 9222, 9221, 9218, 9213,
              9213, 9212, 9210, 9209, 9207, 9206, 9204, 9203, 9202, 9200, 9199, 9198, 9197, 9196, 9195, 9193, 9191,
              9188, 9187, 9183, 9181, 9176, 9174, 9173, 9170, 9168, 9167, 9166, 9158, 9156, 9151, 9150, 9148, 9140,
              9139, 9129, 9126, 9117, 9112, 9108, 9102, 9101, 9099, 9088, 9081, 9080, 9079, 9078, 9076, 9075, 9072,
              9071, 9070, 9067, 9058, 9055, 9051, 9045, 9042, 9037, 9036, 9034, 9034, 9033, 9032, 9017, 9013, 9008,
              9008, 9007, 9005, 9002, 9000, 8996, 8993, 8992, 8989, 8988, 8984, 8977, 8976, 8975, 8973, 8966, 8963,
              8961, 8958, 8956, 8951, 8947, 8946, 8945, 8935, 8930, 8924, 8923, 8920, 8912, 8909, 8902, 8899, 8890,
              8888, 8885, 8883, 8873, 8871, 8870, 8870, 8869, 8866, 8852, 8851, 8841, 8831, 8829, 8826, 8823, 8821,
              8818, 8817, 8814, 8812, 8809, 8807, 8807, 8806, 8799, 8798, 8790, 8784, 8782, 8776, 8775, 8771, 8767,
              8766, 8755, 8750, 8749, 8749, 8746, 8742, 8741, 8732, 8730, 8719, 8718, 8717, 8709, 8707, 8701, 8699,
              8696, 8689, 8688, 8688, 8687, 8681, 8676, 8673, 8672, 8668, 8662, 8659, 8653, 8652, 8651, 8647, 8645,
              8644, 8642, 8640, 8636, 8630, 8627, 8624, 8621, 8620, 8615, 8612, 8610, 8608, 8602, 8601, 8600, 8597,
              8588, 8586, 8584, 8583, 8581, 8579, 8577, 8576, 8575, 8559, 8559, 8556, 8555, 8553, 8550, 8548, 8547,
              8546, 8543, 8539, 8535, 8534, 8532, 8531, 8527, 8527, 8524, 8522, 8520, 8516, 8511, 8510, 8506, 8505,
              8504, 8496, 8496, 8493, 8492, 8484, 8483, 8482, 8479, 8475, 8471, 8470, 8469, 8465, 8450, 8446, 8445,
              8440, 8439, 8437, 8431, 8429, 8428, 8421, 8412, 8410, 8407, 8405, 8403, 8402, 8402, 8398, 8394, 8391,
              8386, 8384, 8383, 8381, 8378, 8377, 8376, 8375, 8372, 8362, 8357, 8346, 8342, 8338, 8336, 8335, 8331,
              8330, 8329, 8326, 8320, 8315, 8314, 8313, 8309, 8306, 8301, 8297, 8292, 8291, 8287, 8282, 8280, 8278,
              8277, 8275, 8272, 8259, 8258, 8256, 8253, 8252, 8238, 8232, 8228, 8226, 8217, 8211, 8210, 8209, 8207,
              8204, 8202, 8197, 8194, 8190, 8185, 8184, 8178, 8172, 8168, 8167, 8165, 8157, 8152, 8149, 8144, 8133,
              8128, 8124, 8119, 8116, 8114, 8113, 8111, 8108, 8107, 8102, 8099, 8098, 8096, 8090, 8084, 8084, 8079,
              8078, 8077, 8077, 8070, 8048, 8047, 8043, 8041, 8035, 8034, 8033, 8031, 8030, 8029, 8026, 8019, 8016,
              8015, 8015, 8013, 8006, 8005, 8004, 8000, 7996, 7995, 7994, 7988, 7986, 7983, 7982, 7981, 7973, 7969,
              7966, 7965, 7964, 7961, 7960, 7959, 7955, 7950, 7942, 7939, 7932, 7928, 7924, 7922, 7921, 7920, 7919,
              7919, 7902, 7899, 7898, 7896, 7888, 7884, 7878, 7877, 7875, 7874, 7863, 7857, 7856, 7850, 7841, 7833,
              7828, 7825, 7823, 7822, 7820, 7817, 7811, 7805, 7801, 7800, 7796, 7794, 7788, 7786, 7784, 7784, 7777,
              7775, 7773, 7770, 7766, 7763, 7758, 7756, 7756, 7755, 7748, 7748, 7743, 7730, 7728, 7726, 7725, 7723,
              7718, 7718, 7715, 7700, 7694, 7687, 7682, 7670, 7670, 7667, 7664, 7648, 7646, 7645, 7629, 7626, 7622,
              7617, 7615, 7609, 7605, 7604, 7594, 7589, 7584, 7574, 7566, 7561, 7544, 7543, 7542, 7533, 7528, 7518,
              7515, 7514, 7509, 7508, 7507, 7507, 7506, 7497, 7495, 7491, 7483, 7481, 7474, 7464, 7463, 7458, 7444,
              7443, 7440, 7437, 7432, 7427, 7421, 7417, 7407, 7405, 7405, 7401, 7393, 7387, 7386, 7379, 7358, 7356,
              7354, 7347, 7344, 7325, 7312, 7298, 7297, 7295, 7292, 7282, 7260, 7252, 7238, 7222, 7216, 7206, 7202,
              7196, 7196, 7194, 7191, 7170, 7167, 7152, 7150, 7139, 7135, 7133, 7131, 7124, 7111, 7101, 7098, 7073,
              7071, 7048, 7027, 7014, 7010, 7007, 7006, 7006, 7004, 7003, 6996, 6993, 6992, 6977, 6963, 6959, 6952,
              6948, 6939, 6911, 6907, 6903, 6896, 6895, 6886, 6850, 6849, 6845, 6845, 6844, 6836, 6836, 6833, 6789,
              6762, 6762, 6751, 6742, 6733, 6733, 6706, 6688, 6671, 6667, 6660, 6645, 6626, 6617, 6611, 6580, 6572,
              6560, 6516, 6505, 6501, 6482, 6478, 6476, 6466, 6461, 6438, 6434, 6430, 6411, 6411, 6395, 6393, 6350,
              6344, 6341, 6338, 6331, 6329, 6323, 6321, 6315, 6315, 6310, 6301, 6297, 6296, 6291, 6272, 6268, 6258,
              6257, 6251, 6248, 6231, 6229, 6226, 6219, 6213, 6202, 6199, 6198, 6196, 6193, 6192, 6190, 6178, 6170,
              6167, 6162, 6158, 6157, 6155, 6150, 6150, 6149, 6147, 6144, 6139, 6138, 6135, 6128, 6127, 6126, 6115,
              6113, 6094, 6093, 6092, 6091, 6088, 6087, 6086, 6080, 6075, 6073, 6067, 6067, 6058, 6057, 6056, 6053,
              6049, 6048, 6045, 6039, 6038, 6034, 6034, 6030, 6017, 6002, 6000, 5999, 5996, 5995, 5964, 5957, 5955,
              5952, 5946, 5924, 5910, 5909, 5908, 5907, 5904, 5890, 5847, 5831, 5830, 5815, 5811, 5785, 5758, 5755,
              5753, 5753, 5749, 5737, 5735, 5721, 5702, 5680, 5666, 5664, 5660, 5652, 5650, 5639, 5629, 5624, 5619,
              5617, 5617, 5606, 5601, 5585, 5577, 5566, 5555, 5530, 5485, 5485, 5470, 5470, 5448, 5437, 5435, 5421,
              5398, 5389, 5376, 5368, 5331, 5309, 5230, 5174, 5130, 5114, 5106, 5090, 5075, 5049, 5039, 5039, 5017,
              5008, 5002, 4999, 4977, 4949, 4941, 4928, 4928, 4925, 4911, 4837, 4827, 4818, 4815, 4815, 4744, 4743,
              4733, 4713, 4709, 4703, 4684, 4659, 4649, 4642, 4606, 4579, 4576, 4572, 4551, 4549, 4545, 4532, 4504,
              4481, 4478, 4476, 4473, 4453, 4449, 4441, 4439, 4391, 4373, 4355, 4322, 4301, 4230, 4190, 4175, 4119,
              4068, 4056, 4056, 4042, 3987, 3980, 3968, 3948, 3921, 3880, 3863, 3861, 3733, 3716, 3670, 3613, 3604,
              3599, 3589, 3497, 3386, 3285, 3176, 3174, 3140, 3107, 3031, 3003, 2950, 2940, 2742, 2704, 2689, 2612,
              2527, 2486, 2460, 2406, 2334, 2324, 2287, 2271, 2254, 2118, 2064, 2041, 2039, 2034, 2025, 1974, 1949,
              1936, 1930, 1917, 1906, 1890, 1875, 1844, 1746, 10480, 10479, 10478, 10477, 10476, 10475, 10474, 10473,
              10472, 10471, 10470, 10469, 10468, 10467, 10466, 10464, 10463, 10462, 10461, 10460, 10459, 10458, 10457,
              10456, 10455, 10454, 10453, 10452, 10451, 10450, 10449, 10448, 10447, 10446, 10445, 10444, 10443, 10442,
              10441, 10440, 10439, 10438, 10437, 10436, 10435, 10434, 10433, 10432, 10431, 10430, 10429, 10428, 10427,
              10426, 10425, 10424, 10423, 10422, 10420, 10419, 10419, 10418, 10417, 10415, 10414, 10413, 10412, 10411,
              10410, 10409, 10408, 10407, 10406, 10405, 10404, 10403, 10402, 10401, 1040, 10399, 10398, 10397, 10396,
              10395, 10394, 10392, 10391, 10389, 10388, 10387, 10386, 10385, 10384, 10383, 10382, 10381, 10380, 10379,
              10378, 10377, 10375, 10374, 10373, 10372, 10371, 10370, 10369, 10368, 10367, 10365, 10364, 10363, 10362,
              10361, 10360, 10359, 10358, 10357, 10356, 10355, 10354, 10353, 10352, 10351, 10350, 10344, 10343, 10342,
              10341, 10340, 10339, 10339, 10338, 10337, 10336, 10335, 10333, 10332, 10331, 10330, 10329, 10328, 10327,
              10326, 10324, 10323, 10322, 10322, 10321, 10320, 10319, 10318, 10317, 10316, 10315, 10314, 10312, 10311,
              10310, 10309, 10308, 10307, 10306, 10305, 10304, 10303, 10302, 10300, 10299, 10298, 10297, 10295, 10294,
              10292, 10291, 10290, 10289, 10288, 10287, 10286, 10285, 10284, 10283, 10282, 10281, 10280, 10279, 10278,
              10277, 10276, 10275, 10274, 10273, 10272, 10271, 10270, 10269, 10268, 10267, 10266, 10265, 10264, 10263,
              10262, 10261, 10260, 10259, 10258, 10257, 10256, 10254, 10253, 10252, 10252, 10251, 10250, 10249, 10248,
              10247, 10246, 10245, 10243, 10242, 10241, 10240, 10239, 10237, 10236, 10235, 10233, 10232, 10231, 10230,
              10229, 10228, 10227, 10226, 10225, 10224, 10223, 10222, 10221, 10220, 10219, 10218, 10217, 10216, 10215,
              10214, 10213, 10212, 10211, 10210, 10209, 10209, 10208, 10207, 10206, 10205, 10204, 10203, 10202, 10202,
              10201, 10200, 10198, 10197, 10196, 10195, 10194, 10193, 10192, 10191, 10190, 10189, 10188, 10187, 10186,
              10185, 10184, 10183, 10181, 10180, 10179, 10178, 10177, 10176, 10175, 10174, 10173, 10171, 10170, 10169,
              10168, 10166, 10165, 10164, 10163, 10162, 10161, 10160, 10159, 10157, 10155, 10154, 10153, 10152, 10150,
              10149, 10148, 10147, 10146, 10145, 10144, 10143, 10142, 10141, 10140, 10139, 10138, 10137, 10136, 10135,
              10134, 10134, 10133, 10132, 10131, 10130, 10129, 10128, 10127, 10126, 10125, 10124, 10122, 10121, 10120,
              10119, 10118, 10117, 10116, 10115, 10114, 10114, 10113, 10111, 10109, 10108, 10107, 10106, 10105, 10103,
              10102, 10101, 10100, 10099, 10098, 10098, 10096, 10095, 10093, 10092, 10091, 10090, 10089, 10088, 10087,
              10086, 10085, 10085, 10083, 10083, 10082, 10081, 10080, 10078, 10077, 10076, 10075, 10074, 10073, 10072,
              10071, 10071, 10070, 10069, 10068, 10067, 10067, 10066, 10064, 10062, 10061, 10061, 10060, 10059, 10057,
              10056, 10055, 10054, 10052, 10052, 10051, 10049, 10048, 10047, 10046, 10045, 10044, 10043, 10042, 10041,
              10040, 10038, 10037, 10036, 10035, 10034, 10033, 10032, 10031, 10030, 10029, 10028, 10027, 10026, 10025,
              10024, 10023, 10022, 10021, 10020, 10019, 10017, 10016, 10015, 10014, 10013, 10012, 10011, 10010, 10009,
              10008, 10007, 10006, 10005, 10004, 10003, 10002, 10001]
# categories = [1746]
for i in categories:

    filename = str(i) + '.txt'
    file = pathlib.Path(filename)
    if not file.exists():
        break

    with open(filename) as file:
        soup = BeautifulSoup(file, "html.parser")
    try:
        html = soup.body.find('dl', class_='dl-horizontal')
        websites = html.find_all('a')
        actual_website = []
        for website in websites:
            website = website.text.strip('\n ')
            actual_website.append(website)

        # for row in rows:
        #     name = row.h2.text.strip("\xa0 Verified SellerUnverified Seller")
        #     # breakpoint()
        #
        #     address = row.find("div", {"class": "col-sm-6 address-info"}).contents
        #     whole_address = (address[1] + ' ' + address[3] + ' ' + address[6]).strip('C/')
        #     try:
        #         website = row.div.a['href']
        #     except:
        #         website = "website"
        #     try:
        #         telephone = row.find("div", {"class": "col-sm-6 contact-info"}).a.text.replace(' ', '')
        #     except:
        #         telephone = "telephone"
        writer.writerow([i, actual_website])
        print([i, actual_website])
    except AttributeError:
        print("issue")
        continue
    # print(i)

outfile.close()
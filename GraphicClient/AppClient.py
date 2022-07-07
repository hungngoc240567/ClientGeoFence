from math import fabs
from turtle import width
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Point, Line
from random import random as r
from functools import partial
# Thay đường dẫn của mọi người đến thư mục này hen
import sys

from numpy import ones_like
sys.path.append('/Users/lap13994/Documents/FinalGeoFenceProject/ClientGeoFence/')
from GraphicClient.VehicleLayout import *
from GraphicClient.GeoFenceLayout import *


class AppGeoFenceClient(App):

    def addGeoFence(self, *largs):
        self.geoFenceMgr.addGeoFence(1)
        self.geoFenceLayout.drawListGeoFence(self.geoFenceMgr)

    def addVehicleX10(self, *largs):
        self.vehicleMgr.addVehicle(10)

    def setInfoMgr(self, geoFenceMgr, vehicleMgr):
        self.geoFenceMgr = geoFenceMgr
        self.vehicleMgr = vehicleMgr

    def updateListGeoFence(self, dt):
        self.geoFenceLayout.drawListGeoFence(self.geoFenceMgr)

    def updateListVihcle(self, dt):
        self.vehicleLayout.drawListVehicle(self.vehicleMgr.getListVehicle(), self.geoFenceMgr)

    def drawTest(self):
        self.drawLayout.canvas.clear()
        points = [797.0277836510518, 100.01104273995884, 803.5276952545803, 100.01555609475156, 804.0024699294343, 100.02002520818127, 809.252424663099, 100.10702352022525, 811.5060717009081, 100.16552135413139, 813.7988706347896, 100.23808189222882, 829.6939007051858, 101.10368231718337, 846.9489305921975, 102.7648078074539, 848.5613813985206, 102.95870210182488, 853.4376115920686, 103.5855430646667, 859.0203379563875, 104.37821128315767, 867.9161928380727, 105.80792657591184, 896.6411385230908, 111.8499126047235, 905.1023587755014, 114.05506327997284, 913.4648445437836, 116.43028136640527, 917.9769286456603, 117.79397662080629, 928.5782514872795, 121.22878508989902, 929.9104413330003, 121.68362811971105, 938.800257655822, 124.85404377139093, 948.6072962103772, 128.62973797967987, 953.508109059021, 130.62856031749868, 961.9032107755122, 134.23046827191843, 962.5041705823802, 134.49706629996433, 974.3077361921738, 139.97664922458216, 975.073580490518, 140.34844444347226, 975.1275391294712, 140.37471579648974, 996.1125525200415, 151.3743171479273, 997.957008731984, 152.418322269592, 1007.5202004527779, 158.04186454473864, 1051.9001827544928, 189.2809984435243, 1112.8021788917342, 250.69136220222228, 1157.9405753993442, 321.45436302506187, 1163.104019588201, 332.20407943310613, 1168.8155546154564, 345.1610944442797, 1170.9016254982291, 350.2268909223976, 1182.4959025947348, 617.033689586542, 1150.1545415536075, 693.3695866194655, 1116.1333517359803, 745.0708140929372, 1104.984324988795, 758.8137583497623, 1078.9297908556905, 786.7022353822878, 1072.8059765708977, 792.535295557987, 1054.3497282742562, 808.7170480015835, 1022.3846070597626, 832.483212422635, 1020.8679605367208, 833.492644609067, 1015.5003312157323, 836.9860638749171, 1002.6997390052188, 844.8373758849469, 1000.3496919123911, 846.2080313202019, 997.3938784954948, 847.901791792606, 990.2118975078686, 851.8798574037112, 984.7150651060947, 854.7962016747801, 969.9923557609172, 862.0809287753965, 943.7141294045923, 873.2911049160964, 922.4489586637599, 880.7968651685053, 823.5034862889756, 899.308885616466, 813.8340956084262, 899.7607006681584, 772.4831762718288, 899.0524081018842, 745.7607804565296, 896.3055728390849, 742.7456817462394, 895.8812234007785, 731.8061162774081, 894.1441287433186, 729.5505861019317, 893.7472286650645, 726.9925712978502, 893.2809623593552, 707.5109008583577, 889.160335260375, 680.6887841416354, 881.7916103981316, 649.0253027836352, 870.4141476785504, 623.4558795716268, 858.9319901348612, 618.9850287260983, 856.6981639631869, 617.051092347339, 855.7101308491201, 613.7147288744433, 853.9742896901946, 600.0287446791627, 846.4267556719725, 588.6855444980597, 839.6265609399808, 568.8824445074688, 826.4730854804983, 550.0203327583115, 812.2661780688627, 506.54949108446067, 771.8212626289765, 497.5620673137049, 761.7848293397462, 473.0433519177682, 730.4329626482106, 472.8455345631396, 730.1520274616805, 458.17623931532194, 707.7414658448909, 453.1127107338102, 699.1713045234046, 452.2392555818252, 697.6422643103365, 405.86642415938684, 568.2548488760443, 413.85804874057067, 395.62378873727744, 417.2112200269728, 383.92782449371697, 426.72234983619046, 356.250927348436, 499.42986002635223, 236.07275442610745, 503.85572528521334, 231.11606862132322, 505.6597104032991, 229.1424840988712, 517.8444594663498, 216.47178104082184, 525.2514210237816, 209.2884275599805, 559.6908523269292, 180.23209425484515, 571.5142409062895, 171.67964136933136, 625.0418495861716, 140.2922775310875, 626.9348426983578, 139.37768880980502, 634.7770418864093, 135.71800193779183, 643.2748416704234, 131.98203203298738, 663.6416605761743, 123.95957229364717, 714.856241704994, 109.16686370856218, 717.5136791533499, 108.59738519884223, 734.1531912425526, 105.45697601343886, 735.6614818321575, 105.20821300340327, 780.9022594848294, 100.45616472380004]
        pointsTest = [[648.1665226172759, 471.54365432933474], [1094.1938929850803, 651.1752758923883], [891.5071602105793, 814.1877865925348], [935.1928964691393, 577.0095787192749], [725.9139439162966, 416.3590436463168], [656.2530437607099, 445.6576711733951], [534.5963474409685, 159.63955846448573], [877.369824445117, 164.88939518067968], [425.5368832621, 691.1619420600986], [968.6545428856159, 671.4235690250521], [1138.6889247906524, 355.58039934062253], [402.92656513883185, 839.2841613926478], [664.9045356518083, 888.0088715750155], [686.039215601505, 448.2324224684799], [967.7792005877094, 580.0114909539541], [571.3600767241652, 623.9696006398772], [973.818413900879, 523.6988750954249], [426.54561574755917, 742.273198247185], [1145.550392606947, 206.95290902474846], [957.4682000148539, 344.69861803056847], [676.4274418108139, 575.7710855781997], [1005.8729677261265, 543.9468201174743], [1045.577771582217, 897.6903825147047], [824.06015487356, 102.46723565745594], [944.687809305963, 753.2194259822932], [1091.6078091583895, 848.334192060541], [638.5141526256177, 250.17642074254684], [1175.8680829674818, 147.90343526942104], [644.7428828594717, 498.7989104187927], [1149.6893138806076, 385.2246793663984], [1018.1328296881834, 103.46065278360993], [866.5348474891069, 403.6541008183627], [1098.0979608691648, 319.79882454781796], [1154.888200425734, 445.58024442468974], [528.1029736908599, 394.02456630268443], [530.5529040898191, 681.6449880053342], [1079.4649348453001, 644.157666897729], [937.174414257263, 751.3100496074383], [511.37233316038873, 460.89548428222145], [712.0295072891387, 242.08872841622656], [773.1519500546743, 798.794944378601], [635.8484948605673, 115.23056314622613], [904.0325381407306, 696.4148177835577], [1162.1529056747713, 741.1159801454038], [409.87295362954285, 507.0347096258977], [933.3114642911819, 238.08642742370262], [895.5416256774683, 439.5356418195156], [877.234784195776, 413.9044523557401], [705.8521105370137, 501.9958917230449], [940.3486072410594, 389.50660702149884], [477.1792128155694, 608.524614594645], [649.2039823732924, 740.1811600525095], [826.0982078754885, 252.82445695045283], [1004.8016633176303, 119.77124879792177], [900.6088102381962, 169.94309049613457], [900.4261924079408, 238.97255903353766], [593.7239861705618, 200.64234978179036], [715.5049386873804, 549.2640037956169], [1068.4228634194862, 140.78260802420118], [974.7249342292334, 239.47783980703002], [667.1853095206955, 501.0882805773793], [573.3599710276061, 182.48504655724662], [1078.5449369329503, 620.6297162938076], [1056.4787677660916, 874.9402748185283], [607.315405327835, 870.3251492629765], [401.4238317450753, 193.4993807168321], [744.3645632233026, 150.73493386632833], [489.66949708152765, 546.3914865063607], [956.0288172423873, 331.389511190284], [965.8861702819544, 329.6959585075638], [712.4793324159102, 896.8611313685603], [468.75674984357454, 703.1439298781585], [848.5704987530531, 257.7576300884108], [679.8099235351852, 780.7321613304791], [799.9194524089194, 552.7862568274493], [473.25357352669334, 786.9062961952637], [881.1846731695387, 311.00339913287416], [661.5106581189895, 359.53894848762604], [1172.7298386198668, 461.335248143096], [817.8782470413378, 786.3970182087736], [756.0786907333143, 669.4231459180572], [819.4495936664403, 342.2614298403669], [587.7844440714223, 849.8162006400247], [1090.1573485370363, 649.330827913092], [1025.5568125881312, 544.5020480365138], [635.5153643067433, 714.0101635359778], [919.7081216461902, 276.7360573122535], [847.3548191208973, 798.6533028816901], [457.19878875713164, 382.0975386393711], [518.5693340560546, 167.29777363065693], [594.7809735742542, 186.67035922081197], [744.6024268252336, 599.8985488462722], [1141.9586068931012, 545.2143750370404], [1000.1296841910162, 600.036325842779], [953.6999137392709, 870.1624011452861], [466.10617387088644, 226.54485325615462], [467.0579153603602, 275.2465768610167], [844.0691300660903, 659.9700979877623], [565.0728806644194, 525.5266458526498], [831.3040217576208, 770.2434276767311], [875.5494914543854, 528.5611035413053], [542.2013125904024, 282.41901047491444], [1111.5203015942566, 119.43152154777749], [447.8497692909299, 442.7951750917284], [934.4256219059876, 485.298423976076], [667.6308946786424, 368.20747858737707], [1070.259072680317, 543.1364260665778], [1083.2980587255038, 516.7505224820859], [633.1463671250152, 527.2647229783286], [1157.7422469591957, 748.6539817278597], [410.0439596701938, 761.2579729691734], [527.3655418300272, 851.5072845484882], [834.4628326303873, 281.79109407149815], [998.701878223806, 184.49597426059756], [926.341356282395, 649.9407501289027], [1116.6433419861005, 651.7815929899182], [599.4102105051644, 128.43439765367543], [783.3495485461224, 345.6255702229091], [1036.6105252038974, 821.3071550978748], [1093.6354924585462, 705.326803561079], [708.3459348606485, 765.3949493279702], [814.3530000162459, 318.51051328796143], [457.56720524850846, 331.0616076471774], [571.9987313289383, 746.775612016381], [699.9075532156788, 832.5259856395953], [824.5013562674553, 788.1759655800141], [1186.3047513362167, 166.12411503451654], [879.8583272691528, 594.4800110215115], [549.7657471820831, 387.81005413580806], [786.0122985956953, 841.6216565260761], [607.1475179781636, 209.16804336255052], [653.0752391607367, 707.2244443100373], [1111.04705071827, 234.17698292652312], [480.72775394338896, 539.5495975196968], [1146.111861543678, 376.9372672760294], [650.3391824090002, 807.6869630195275], [438.301621855882, 493.53879719892115], [903.0733515597731, 603.2774698249511], [694.8494064288991, 429.21749771681743], [1061.9632089413162, 619.5234007381721], [516.8909201451886, 824.9164584010547], [767.6566041464997, 763.712408698718], [625.9477894708821, 745.3370613128075], [484.2541532013462, 164.94959273356824], [1119.6703417404447, 483.5332511455059], [1193.3786113449394, 519.2604163290677], [821.4639270778373, 565.0718655546962], [731.3344498007812, 869.6967453016174], [512.8415868848559, 217.7500690573603], [1035.9345572785487, 249.5462755794655], [536.5644650962003, 390.82969816687563], [656.2900387286486, 522.2147124863052], [932.8502706721483, 600.7175736291628], [1140.577829809057, 431.8190600459281], [520.1489267618741, 647.9888392054504], [1153.5194167449413, 533.9984112780592], [556.2031048095388, 793.6199468257828], [1187.0228603663654, 506.91823758659183], [814.3300697447319, 500.2658899105958], [914.158985972521, 547.9122338693526], [684.0803102707197, 737.3856227739027], [598.3615060504518, 341.675063479709], [454.64678285932325, 516.98802930438], [706.459335121079, 841.3875152217813], [663.6177137334099, 769.7397252395199], [1185.8682934023566, 634.6249339020198], [1092.8843493554866, 689.1444893124385], [952.9880633128707, 771.3681112186082], [867.733943311039, 464.4733280072788], [1001.5691846100027, 811.9048654021751], [1164.3771510618403, 291.09227462622846], [1176.5333229882394, 507.8789251198163], [1055.3773850893754, 689.8044734812755], [670.4490603761736, 760.211884309983], [621.6688131493255, 284.7912816725815], [886.5839720024777, 303.0925508424916], [434.0682265706961, 682.7061202653337], [874.1729199608751, 543.6966526886969], [856.4047386180177, 763.4437058166003], [478.2605769571536, 142.76890058589765], [746.6102902595633, 136.0756749005651], [658.1956886417161, 851.6678465502152], [1031.3321097604185, 131.41264678557525], [515.5727346844691, 826.9429912845276], [703.8478583230492, 895.6214871344683], [434.1357225115032, 323.9820599752454], [644.2821686137623, 117.29510542365404], [770.8775320928302, 126.73563223874294], [1085.3423882548009, 263.34112483191996], [549.286954500865, 100.99414885139379], [1146.0101934010258, 517.0242758044742], [992.4142119410835, 664.162277813251], [429.8441833851066, 504.46633702561894], [495.14481326834834, 144.9431753014194], [833.7676074639087, 163.87603374873584], [1171.789954156559, 361.81485311813867], [1037.43392412682, 554.749980172104], [426.8206979132656, 479.6489916843722], [1042.4817032525862, 422.25488936225395], [483.29187006669804, 109.29169139296164]]
        true = True
        false = False
        print("len of list convex ", len(points))
        listInOut = [true, true, true, true, true, true, false, true, false, true, true, false, false, true, true, true, true, false, false, true, true, true, false, true, true, false, true, false, true, true, false, true, true, true, true, true, true, true, true, true, true, false, true, false, true, true, true, true, true, true, true, true, true, false, true, true, true, true, false, true, true, true, true, false, false, false, true, true, true, true, false, true, true, true, true, false, true, true, true, true, true, true, false, true, true, true, true, true, true, false, true, true, true, true, false, false, false, true, true, true, true, true, false, true, true, true, true, true, true, false, false, false, true, true, true, true, false, true, true, true, true, true, true, true, true, true, false, true, true, true, true, true, false, true, true, true, true, true, true, true, false, true, true, false, true, false, true, true, false, true, true, true, true, true, true, true, true, false, true, true, true, true, true, true, true, false, true, true, true, true, false, true, true, true, true, true, false, true, true, false, true, true, false, false, false, false, false, true, true, false, true, true, true, false, true, false, true, true, true, false]
        with self.drawLayout.canvas:
            Line(points = points, width = 1)
            for i in  range(len(pointsTest)):
                point = pointsTest[i]
                color = 0.5
                if listInOut[i] == True:
                    color = 1
                Color(color, 1, 1, mode = 'hsv')
                Rectangle(pos = (point[0], point[1]), size = (20, 20))


    def build(self):
        self.drawLayout = FloatLayout()
        self.drawTest()
        # self.geoFenceLayout = GeoFenceLayout()
        # self.geoFenceLayout.setInit()
        # self.vehicleLayout = VehicleLayout()

        # self.btnAddGeoFence = Button(text = 'add Geo Fence', on_press = partial(self.addGeoFence))
        # self.btnAddVehiclex10 = Button(text = 'add Vehicle x10', on_press = partial(self.addVehicleX10))
        # layoutBtn = BoxLayout(size_hint=(1, None), height=50)
        # layoutBtn.add_widget(self.btnAddGeoFence)
        # layoutBtn.add_widget(self.btnAddVehiclex10)

        # root = BoxLayout(orientation='vertical')
        # root.add_widget(self.drawLayout)
        # self.drawLayout.add_widget(self.geoFenceLayout)
        # self.drawLayout.add_widget(self.vehicleLayout)
        # root.add_widget(layoutBtn)
        # print("size of me", root.size)

        # Clock.schedule_interval(self.updateListGeoFence, 0.1)
        # Clock.schedule_interval(self.updateListVihcle, 0.1)

        return self.drawLayout
        

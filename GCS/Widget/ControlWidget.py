
from GCS.Widget.BaseWidget import BaseWidget
from PyQt5.QtWidgets import QWidget,QVBoxLayout
from GCS.Util.Util import *
from GCS.Module.ControlModule import ControlModule
from GCS.Module.DroneModule import DroneModule
from GCS.Module.WaypointModule import WaypointModule


class ControlWidget(BaseWidget):

    def __init__(self):

        super(ControlWidget, self).__init__(CONTROL_WIDTH, CONTENTS_HEIGHT, CONTROL_WIDGET_COLOR)

        # 위젯들(버튼컨트롤, 접속정보, Waypoint) > 레이아웃
        self.control_layout = QVBoxLayout(self.widget)

        self.control_module = ControlModule()
        self.drone_module = DroneModule()
        self.way_point_module = WaypointModule()

        # UI 설정
        self.init_widget()

    # #########################################################################################
    #  Widget 초기화 및 설정
    # #########################################################################################
    def init_widget(self):

        # 레이아웃 옵션 설정
        self.control_layout.setContentsMargins(0, 0, 0, 0)

        # 위젯 인스턴스 > 레이아웃
        self.control_layout.addWidget(self.control_module)
        self.control_layout.addWidget(self.drone_module)
        self.control_layout.addWidget(self.way_point_module)

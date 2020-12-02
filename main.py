from PyQt5 import QtWidgets

if __name__ == "__main__":
    
    # Initialize Qt
    app = QtWidgets.QApplication([])

    # create the QMainWindow and add both widgets
    win = QtWidgets.QMainWindow()
    win.setWindowTitle("Interface trajectoire drone")
    #win.setCentralWidget(rad)
    win.addDockWidget(QtCore.Qt.DockWidgetArea(1), insp_dock)
    # win.resize(1000, 600)
    # win.show()
    win.showMaximized()

    # create the second view
    # second_view = radarview.PanZoomView(main_window.scene)
    # second_view.scale(0.1, -0.1)
    # second_view.show()
    # second_view.move(300, 300)

    # enter the main loop
    app.exec_()
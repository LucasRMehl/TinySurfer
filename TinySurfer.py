''' A tiny web browser '''

import sys

from PyQt4 import QtGui, QtCore, QtWebKit

class TinySurfer(QtGui.QMainWindow):
    ''' A tiny web browser written in PyQt4 '''
    def __init__(self, url):
        super(TinySurfer, self).__init__()

        ### Window elements ###
        prog_bar = QtGui.QProgressBar()
        prog_bar.setMaximumWidth(120)

        self.web_view = QtWebKit.QWebView(loadProgress=prog_bar.setValue,
                                          loadFinished=prog_bar.hide,
                                          loadStarted=prog_bar.show,
                                          titleChanged=self.setWindowTitle)

        toolbar = self.addToolBar("")  # Only returns a QToolbar object if given a title...
        for action in (QtWebKit.QWebPage.Back, QtWebKit.QWebPage.Forward, QtWebKit.QWebPage.Reload):
            toolbar.addAction(self.web_view.pageAction(action))
        url_line = QtGui.QLineEdit(returnPressed=lambda: self.web_view.setUrl(QtCore.QUrl.fromUserInput(url_line.text())))
        url_line.setStyleSheet("font-size:15px;")
        toolbar.addWidget(url_line)
        
        search_bar = QtGui.QLineEdit(returnPressed=lambda: self.web_view.findText(search_bar.text()))
        search_bar.hide()

        status_bar = self.statusBar()
        status_bar.addPermanentWidget(search_bar)
        status_bar.addPermanentWidget(prog_bar)

        self.setCentralWidget(self.web_view)
        self.web_view.load(url)

        # Handle QWebView events
        self.web_view.urlChanged.connect(lambda u: url_line.setText(u.toString()))
        self.web_view.urlChanged.connect(self.url_completer)
        self.web_view.statusBarMessage.connect(status_bar.showMessage)
        self.web_view.page().linkHovered.connect(lambda l: status_bar.showMessage(l, 3000))
        self.web_view.settings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled, True)

        # Keyboard shortcuts
        QtGui.QShortcut(QtGui.QKeySequence.Find, self, activated=lambda: (search_bar.show(), search_bar.setFocus()))
        QtGui.QShortcut("Esc", self, activated=lambda: (search_bar.hide(), self.web_view.setFocus()))
        QtGui.QShortcut("Ctrl+Q", self, activated=self.close)
        QtGui.QShortcut("Ctrl+F4", self, activated=self.close)
        QtGui.QShortcut(QtGui.QKeySequence.Refresh, self, activated=self.web_view.reload)
        QtGui.QShortcut(QtGui.QKeySequence.Back, self, activated=self.web_view.back)
        QtGui.QShortcut(QtGui.QKeySequence.Forward, self, activated=self.web_view.forward)
        QtGui.QShortcut(QtGui.QKeySequence.ZoomIn, self, activated=lambda: self.web_view.setZoomFactor(self.web_view.zoomFactor()+.2))
        QtGui.QShortcut(QtGui.QKeySequence.ZoomOut, self, activated=lambda: self.web_view.setZoomFactor(self.web_view.zoomFactor()-.2))
        QtGui.QShortcut("Ctrl+=", self, activated=lambda: self.web_view.setZoomFactor(1))

    def url_completer(self):
        ''' Autocomplete functionality for URL bar '''
        # Just use the history for now
        str_list = [QtCore.QString(i.url().toString()) for i in self.web_view.history().items()]
        return QtGui.QCompleter(QtCore.QStringList(str_list),
                                caseSensitivity=QtCore.Qt.CaseInsensitive)


if __name__ == "__main__":
    APP = QtGui.QApplication(sys.argv)
    if len(sys.argv) > 1:
        URL = QtCore.QUrl.fromUserInput(sys.argv[1])
    else:
        URL = QtCore.QUrl('http://www.python.org')
    BROWSER = TinySurfer(URL)
    BROWSER.show()
    sys.exit(APP.exec_())

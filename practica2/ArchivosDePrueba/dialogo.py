#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.5 on Thu Apr 23 16:41:10 2020
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MiVentana(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MiVentana.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((700, 507))
        self.newsheet_button = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("C:\\Users\\eldkt\\Downloads\\project-20200412T022146Z-001\\project\\icons\\newsheet.ico", wx.BITMAP_TYPE_ANY))
        self.open_button = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("C:\\Users\\eldkt\\Downloads\\project-20200412T022146Z-001\\project\\icons\\abrir.ico", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_1 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("C:\\Users\\eldkt\\Downloads\\project-20200412T022146Z-001\\project\\icons\\save.ico", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_undo = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("C:\\Users\\eldkt\\Downloads\\project-20200412T022146Z-001\\project\\icons\\undo.ico", wx.BITMAP_TYPE_ANY))
        self.radio_btn_2048 = wx.RadioButton(self, wx.ID_ANY, "")
        self.radio_btn_abc = wx.RadioButton(self, wx.ID_ANY, "")
        self.radio_btn_nivel = wx.RadioButton(self, wx.ID_ANY, "")
        self.radio_btn_1024 = wx.RadioButton(self, wx.ID_ANY, "")
        self.matrix = wx.Panel(self, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnSaveClick, self.bitmap_button_1)
        self.Bind(wx.EVT_RADIOBUTTON, self.dic2048, self.radio_btn_2048)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MiVentana.__set_properties
        self.SetTitle("frame")
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.newsheet_button.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.newsheet_button.SetSize(self.newsheet_button.GetBestSize())
        self.open_button.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.open_button.SetSize(self.open_button.GetBestSize())
        self.bitmap_button_1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bitmap_button_1.SetSize(self.bitmap_button_1.GetBestSize())
        self.bitmap_button_undo.SetMinSize((48, 48))
        self.bitmap_button_undo.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.radio_btn_nivel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        self.matrix.SetMinSize((370, 300))
        self.matrix.SetBackgroundColour(wx.Colour(0, 0, 0))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MiVentana.__do_layout
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_2 = wx.GridSizer(3, 3, 0, 0)
        sizer_1 = wx.GridSizer(1, 1, 0, 0)
        grid_sizer_1 = wx.GridSizer(3, 3, 0, 0)
        sizer_4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "MODO"), wx.HORIZONTAL)
        grid_sizer_5 = wx.GridSizer(4, 2, 0, 0)
        grid_sizer_3 = wx.GridSizer(2, 1, 0, 0)
        grid_sizer_4 = wx.GridSizer(1, 3, 0, 0)
        grid_sizer_4.Add(self.newsheet_button, 0, wx.EXPAND | wx.LEFT | wx.TOP, 10)
        grid_sizer_4.Add(self.open_button, 0, wx.EXPAND | wx.LEFT | wx.TOP, 10)
        grid_sizer_4.Add(self.bitmap_button_1, 0, wx.EXPAND | wx.LEFT | wx.TOP, 10)
        grid_sizer_3.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_2.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        grid_sizer_2.Add(self.bitmap_button_undo, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.LEFT, 53)
        label_2048 = wx.StaticText(self, wx.ID_ANY, "2048")
        label_2048.SetFont(wx.Font(12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, 0, "Comic Sans MS"))
        grid_sizer_5.Add(label_2048, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_5.Add(self.radio_btn_2048, 0, wx.ALIGN_CENTER | wx.SHAPED, 0)
        label_abc = wx.StaticText(self, wx.ID_ANY, "ABC")
        label_abc.SetFont(wx.Font(12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, 0, "Comic Sans MS"))
        grid_sizer_5.Add(label_abc, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_5.Add(self.radio_btn_abc, 0, wx.ALIGN_CENTER, 0)
        label_nivel = wx.StaticText(self, wx.ID_ANY, "Nivel")
        label_nivel.SetFont(wx.Font(12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, 0, "Comic Sans MS"))
        grid_sizer_5.Add(label_nivel, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_5.Add(self.radio_btn_nivel, 0, wx.ALIGN_CENTER, 0)
        label_1024 = wx.StaticText(self, wx.ID_ANY, "1024")
        label_1024.SetFont(wx.Font(12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, 0, "Comic Sans MS"))
        grid_sizer_5.Add(label_1024, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_5.Add(self.radio_btn_1024, 0, wx.ALIGN_CENTER, 0)
        sizer_4.Add(grid_sizer_5, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(sizer_4, 0, wx.EXPAND | wx.LEFT, 8)
        bitmap_1 = wx.StaticBitmap(self.matrix, wx.ID_ANY, wx.Bitmap("C:\\Users\\eldkt\\Downloads\\project-20200412T022146Z-001\\project\\icons\\0-7.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(bitmap_1, 0, 0, 0)
        bitmap_2 = wx.StaticBitmap(self.matrix, wx.ID_ANY, wx.Bitmap("C:\\Users\\eldkt\\Downloads\\project-20200412T022146Z-001\\project\\icons\\0-3.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(bitmap_2, 0, 0, 0)
        bitmap_3 = wx.StaticBitmap(self.matrix, wx.ID_ANY, wx.Bitmap("C:\\Users\\eldkt\\Downloads\\project-20200412T022146Z-001\\project\\icons\\0-8.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(bitmap_3, 0, 0, 0)
        bitmap_4 = wx.StaticBitmap(self.matrix, wx.ID_ANY, wx.Bitmap("C:\\Users\\eldkt\\Downloads\\project-20200412T022146Z-001\\project\\icons\\0-6.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(bitmap_4, 0, 0, 0)
        bitmap_5 = wx.StaticBitmap(self.matrix, wx.ID_ANY, wx.Bitmap("C:\\Users\\eldkt\\Downloads\\project-20200412T022146Z-001\\project\\icons\\0-7.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(bitmap_5, 0, 0, 0)
        bitmap_6 = wx.StaticBitmap(self.matrix, wx.ID_ANY, wx.Bitmap("C:\\Users\\eldkt\\Downloads\\project-20200412T022146Z-001\\project\\icons\\0-2.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(bitmap_6, 0, 0, 0)
        bitmap_7 = wx.StaticBitmap(self.matrix, wx.ID_ANY, wx.Bitmap("C:\\Users\\eldkt\\Downloads\\project-20200412T022146Z-001\\project\\icons\\0-8.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(bitmap_7, 0, 0, 0)
        bitmap_8 = wx.StaticBitmap(self.matrix, wx.ID_ANY, wx.Bitmap("C:\\Users\\eldkt\\Downloads\\project-20200412T022146Z-001\\project\\icons\\0-8.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(bitmap_8, 0, 0, 0)
        bitmap_9 = wx.StaticBitmap(self.matrix, wx.ID_ANY, wx.Bitmap("C:\\Users\\eldkt\\Downloads\\project-20200412T022146Z-001\\project\\icons\\1-9.png", wx.BITMAP_TYPE_ANY))
        grid_sizer_1.Add(bitmap_9, 0, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.matrix.SetSizer(sizer_1)
        grid_sizer_2.Add(self.matrix, 1, wx.ALIGN_CENTER | wx.LEFT, 194)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, "AUTORES:\n@Miguel\n@Abdu")
        label_2.SetMinSize((112, 100))
        label_2.SetFont(wx.Font(16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, 0, "Comic Sans MS"))
        grid_sizer_2.Add(label_2, 0, wx.ALIGN_BOTTOM | wx.LEFT, 7)
        label_movs = wx.StaticText(self, wx.ID_ANY, "MOVIMIENTOS: ")
        label_movs.SetFont(wx.Font(12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, 0, "Comic Sans MS"))
        grid_sizer_2.Add(label_movs, 0, wx.ALIGN_CENTER | wx.TOP, 18)
        label_puntos = wx.StaticText(self, wx.ID_ANY, "PUNTOS: ")
        label_puntos.SetFont(wx.Font(12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, 0, "Comic Sans MS"))
        grid_sizer_2.Add(label_puntos, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP, 18)
        sizer_3.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_3)
        self.Layout()
        # end wxGlade

    def OnSaveClick(self, event):  # wxGlade: MiVentana.<event_handler>
        print("Event handler 'OnSaveClick' not implemented!")
        event.Skip()

    def dic2048(self, event):  # wxGlade: MiVentana.<event_handler>
        print("Event handler 'dic2048' not implemented!")
        event.Skip()

# end of class MiVentana

class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.spin_ctrl_1 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_ctrl_2 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("dialog")
        self.SetSize((400, 300))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_6 = wx.GridSizer(2, 1, 0, 0)
        grid_sizer_8 = wx.GridSizer(1, 1, 0, 0)
        grid_sizer_9 = wx.GridSizer(1, 2, 0, 0)
        grid_sizer_7 = wx.GridSizer(1, 2, 0, 0)
        label_1 = wx.StaticText(self, wx.ID_ANY, "Dimension", style=wx.ST_NO_AUTORESIZE)
        label_1.SetFont(wx.Font(12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, 0, "Comic Sans MS"))
        grid_sizer_7.Add(label_1, 0, wx.ALIGN_CENTER | wx.LEFT, 22)
        grid_sizer_7.Add(self.spin_ctrl_1, 0, wx.ALIGN_CENTER, 35)
        grid_sizer_6.Add(grid_sizer_7, 1, wx.EXPAND, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, "Obstaculos")
        label_2.SetFont(wx.Font(12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, 0, "Comic Sans MS"))
        grid_sizer_9.Add(label_2, 0, wx.ALIGN_CENTER | wx.LEFT, 22)
        grid_sizer_9.Add(self.spin_ctrl_2, 0, wx.ALIGN_CENTER, 35)
        grid_sizer_8.Add(grid_sizer_9, 1, wx.EXPAND, 0)
        grid_sizer_6.Add(grid_sizer_8, 1, wx.EXPAND, 0)
        sizer_2.Add(grid_sizer_6, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        self.Layout()
        # end wxGlade

# end of class MyDialog

class MyApp(wx.App):
    def OnInit(self):
        self.dialog = MyDialog(None, wx.ID_ANY, "")
        self.SetTopWindow(self.dialog)
        self.dialog.ShowModal()
        self.dialog.Destroy()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()

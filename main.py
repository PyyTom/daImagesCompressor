from PIL import Image
import flet as fl,os
def main(page:fl.Page):
    d=fl.AlertDialog()
    def xit(e):
        page.window_destroy()
    def select(e:fl.FilePickerResultEvent):
        for i in e.files:
            if i.path[-3:] in ['jpg','jpeg','png']:
                compressed=Image.open(i.path)
                compressed.save((i.path).split('.')[0]+'_compressed.'+(i.path).split('.')[1],optimize=True,quality=90)
                d.title=fl.Text('IMAGE SUCCESSFULLY COMPRESSED')
            else:d.title=fl.Text('INVALID FILE FORMAT')
            page.dialog=d
            d.open=True
            page.update()
        c_original.controls.append(fl.Text(' - '.join(map(lambda f:f.name,e.files)) if e.files else 'CANCELLED'))
        c_original.update()
    picker=fl.FilePicker(on_result=select)
    c_original=fl.Column()
    c_compressed=fl.Column()
    page.overlay.append(picker)
    page.add(fl.Text('IMAGES COMPRESSOR'),
             fl.Row(controls=[
                 fl.ElevatedButton('SELECT',on_click=lambda _:picker.pick_files(allow_multiple=True)),
                 fl.ElevatedButton('EXIT',on_click=xit)]),
             fl.Row(controls=[c_original,c_compressed]))
fl.app(target=main)
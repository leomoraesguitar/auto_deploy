

import flet as ft


class ConfirmarSaida:
    def __init__(self,page, funcao = None):
        super().__init__()
        self.page = page
        self.funcao = funcao
        self.confirm_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirme!"),
            content=ft.Text("Deseja realmente fechar o App?"),
            actions=[
                ft.ElevatedButton("Sim", on_click=self.yes_click),
                ft.OutlinedButton("Não", on_click=self.no_click),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.page.window.on_event = self.window_event
        self.page.window.prevent_close = True 
   


    def window_event(self, e):
            if e.data == "close":
                self.page.overlay.append(self.confirm_dialog)
                
                self.confirm_dialog.open = True
                self.page.update()

    def yes_click(self,e):
        if self.funcao not in ['', None]:
            self.funcao(e)
        self.page.window.destroy()

    def no_click(self,e):
        self.confirm_dialog.open = False
        self.page.update()

class Resize:
    def __init__(self,page):
        self.page = page
        self.page.on_resized = self.page_resize
        self.pw = ft.Text(bottom=10, right=10, theme_style=ft.TextThemeStyle.TITLE_MEDIUM )
        self.page.overlay.append(self.pw)   

    def page_resize(self, e):
        self.pw.value = f'{self.page.window.width}*{self.page.window.height} px'
        self.pw.update()


class Saida(ft.Column):
    def __init__(self, height=150, page = None):
        super().__init__()
        self.page = page
        self._height = height
        self.saidad = ft.Text('', selectable=True)
        self.controls.append(ft.Container(ft.ListView([self.saidad],auto_scroll = True, height=self._height,  ),bgcolor='white,0.08' ))
    def pprint(self, *texto):
        for i in list(texto):
            self.saidad.value += f'{i}\n'
        try:
            self.page.update()
        except:
            pass

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        self._height = height
        try:
            self.controls[0].content.height = self._height
            # print(self.controls[0])
            self.page.update()
        except:
            pass



class ClassName(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls = [ft.Text('Meu ovo')]


def main(page: ft.Page):
    # Definindo o titulo da pagina
    page.title = 'Título'
    page.window.width = 500  # Define a largura da janela como 800 pixels
    page.window.height = 385  # 
    page.theme_mode = ft.ThemeMode.DARK

    ConfirmarSaida(page  = page)
    Resize(page)
    p = ClassName()
    page.add(p,saida)

if __name__ == '__main__': 
    saida = Saida()
    print = saida.pprint 
    ft.app(target=main)


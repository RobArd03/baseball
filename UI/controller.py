import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._v0 = None
        self._year = None
    def handleCreaGrafo(self, e):
        self._view._txt_result.controls.clear()
        self._model.buildGraph(self._year)
        self._view._txt_result.controls.append(ft.Text(f"Grafo creato con successo!", color = "green"))
        self._view._ddSquadra.options.clear()
        for node in self._model._nodes:
            self._view._ddSquadra.options.append(ft.dropdown.Option(key = node.name, data = node, on_click = self.squadV0  ))
        self._view.update_page()

    def squadV0(self, e):
        self._v0 = e.control.data

    def handleDettagli(self, e):
        self._view._txt_result.controls.clear()

        list = self._model.adiacenti(self._v0)
        self._view._txt_result.controls.append(ft.Text(f"Di seguito i dettagli delle squadre e i relativi pesi del collegamento:"))
        for l in list:
            self._view._txt_result.controls.append(ft.Text(f"{l[1]} - {l[0]} "))

        self._view.update_page()

    def handlePercorso(self, e):
        self._view._txt_result.controls.clear()

        bestPath, bestScore = self._model.calcolaPercorso(self._v0)
        self._view._txt_result.controls.append(ft.Text(f"Il costo massimo è {bestScore} di seguito i nodi: "))
        for n in bestPath:
            self._view._txt_result.controls.append(ft.Text(f"{n.name} - {n.peso} "))

        self._view.update_page()

    def fillDDAnno(self):
        for y in self._model.getYear():
            self._view._ddAnno.options.append(ft.dropdown.Option(
                key = y, data = y, on_click = self.data ))

    def stampaSquad(self, e):
        year = self._view._ddAnno.value
        nodes = self._model.getAllNodes(year)
        self._view._txtOutSquadre.controls.clear()
        for i in range(len(nodes)):
            self._view._txtOutSquadre.controls.append(ft.Text(f" Squadra numero {i+1}: {nodes[i].name}"))
        self._view._btnCreaGrafo.disabled = False
        self._view.update_page()

    def data(self, e):
        self._year = e.control.data

    def abilitazione(self, e):
        self._view._btnDettagli.disabled = False
        self._view._btnPercorso.disabled = False
        self._view.update_page()


# DAO Copia incolla per velocizzare
class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllMetodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """"""
        cursor.execute(query)
        for row in cursor:
            result.append(
                Metodo(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllProdotti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """"""
        cursor.execute(query, (method, ))
        for row in cursor:
            result.append(
                Prodotto(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllProfit():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """"""

        cursor.execute(query,)

        for row in cursor:
            result.append(**row)

        cursor.close()
        conn.close()
        return result

# Copia incolla MODEL per fare getCaratteristiche

    def ricorsione(self, parziale, v0):
        if v0 in parziale:
            if self.peso(parziale) > self._costBest:
                self._costBest = self.peso(parziale)
                self._solBest = copy.deepcopy(parziale)

        for v in self._grafo.nodes:
            if v not in self._grafo.neighbors(parziale[-1]):
                if v not in parziale:
                    parziale.append(v)
                    self.ricorsione(parziale, v0)
                    parziale.pop()

    def peso(self, parziale):
        peso = 0
        for nodi in parziale:
            peso += nodi.condiment_calories
        return peso

    def getCaratteristiche(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    #Copia incolla CONTROLLER
    def handle_ingredienti(self, e):
        self._view.txt_result.controls.clear()
        self.ordinare = []
        calorie_str = self._view.txtcalorie.value
        try:
            calorie_float = float(calorie_str)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text(f"Errore nell'inserimento delle calorie!!"))
            self._view.update_page()
            return
        self._model.buildGraph(calorie_float)
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato!"))
        self._model.buildGraph(calorie_float)
        nNodes, nEdges = self._model.getCaratteristiche()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo creato ha {nNodes} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo creato ha {nEdges} archi"))

#nel caso si volesse aggiungere un fillDD nel CONTROLLER
    def fillDD(self):
        self._view.ddingredienti.options.clear()
        for n in self._model._grafo.nodes:
            self._view.ddingredienti.options.append(
                ft.dropdown.Option(data=n, text=n.display_name, on_click=self.readDD))

    def readDD(self, e):
        if e.control.data is None:
            self.choiceIngredient = None
        else:
            self.choiceIngredient = e.control.data

#nel caso in cui mancasse il create alert nel VIEW
    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

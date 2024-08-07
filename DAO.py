# DAO Copia incolla per velocizzare
class DAO():
    def __init__(self):
        pass

    @staticmethod
    def nome1():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """"""
        cursor.execute(query)
        for row in cursor:
            result.append()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def nome2():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """"""
        cursor.execute(query, ())
        for row in cursor:
            result.append(
                )
            #Prodotto(**row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def nome3():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """"""

        cursor.execute(query,)

        for row in cursor:
            result.append()

        cursor.close()
        conn.close()
        return result

# Copia incolla MODEL per fare getCaratteristiche
    def __init__(self):
        self._grafo = nx.Graph()
        self.nodi = []
        self.idMap = {}

    def buildGraph(self):
        self._grafo.clear()
        self.addEdges()

    def addEdges(self):
        self._grafo.clear_edges()

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
        self._model.buildGraph()
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato!"))
        nNodes, nEdges = self._model.getCaratteristiche()
        if nNodes == 0 and nEdges == 0:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione, grafo vuoto."))
            self._view.update_page()
            return
        self._view.txt_result.controls.append(ft.Text(f"Il grafo creato ha {nNodes} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo creato ha {nEdges} archi"))
        self._view.update_page()

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

#query utilizzabile in diversi casi!
select t1.tipo, t2.tipo2, t1.c1, count(distinct t1.c1)
from (select p.food_code as c1, p.portion_display_name as tipo
from food_pyramid_mod.portion p
where p.calories <400) as t1,
(select p.food_code as c2, p.portion_display_name as tipo2
from food_pyramid_mod.portion p
where p.calories <400) as t2
where t1.tipo != t2.tipo2 and t1.c1 = t2.c2 and t1.tipo < t2.tipo2
group by t1.tipo, t2.tipo2


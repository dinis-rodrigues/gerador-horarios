class HTMLErrorPrinter:

    def no_timetables(self):
        return """\
  <body style="margin:15px">
    <div class="mtop1 coutput2" style="line-height: 1.5em;font-family:'Verdana';font-size:12px;color:#DD0000">
      Não há nenhum horário compatível com todas as disciplinas que seleccionou.<br>
      Experimente remover um tipo de aula ou uma disciplina.
    </div>"""
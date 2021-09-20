from tt_generator import *

class HTMLPrettyPrinter:

    def __init__(self):
        self.course_colors = {}
        self.color_gen = color_generator()
        self.table_id = 0

    def color(self, course_name):
        if not course_name in list(self.course_colors.keys()):
            self.course_colors[course_name] = next(self.color_gen)
        return self.course_colors[course_name]

    def print_timetables(self, timetables, total_combinations):
        try:
          print(intro(len(timetables), total_combinations))
          for timetable in timetables:
              self.table_id += 1
              print(self.format_timetable(timetable, self.table_id))
          print(outro())
        except Exception as e:
          print(e)

    def format_timetable(self, timetable, table_id):

        # initialize content for each cell
        content = [["class='period-empty-slot' >&nbsp;" \
                    for x in range(32)] \
                   for y in range(6)]

        # fill out the content according to the lesson slots
        for slot in timetable.lessons:
            day_i = slot.day
            start_i = time_index(slot.start)
            end_i = time_index(slot.end)

            content[day_i][start_i] = "class='period-first-slot' "
            content[day_i][end_i-1] = "class='period-last-slot' "
            for time_i in range(start_i, end_i):
                if time_i > start_i and time_i < end_i-1:
                  content[day_i][time_i] = "class='period-middle-slot' "
                content[day_i][time_i] += "style='background-color: %s'  " \
                                          % (self.color(slot.course_name()))
                content[day_i][time_i] += "headers='weekday%i hour%i'  " \
                                          % (day_i, time_i)
                content[day_i][time_i] += "title='%s-%s'> " \
                                          % (slot.start, slot.end)




            content[day_i][start_i] += "%s&nbsp;&nbsp;(%s)&nbsp;%s" \
                                       % (slot.course_name(), slot.lesson_category(), slot.room)

        # format the HTML for the timetable
        html_result = [table_intro(table_id)]
        for row in range(0,32):
            html_result.append("              <tr>\n")
            html_result.append("                <th  class='period-hours' id='hour%i'>%s-%s</th>\n" % (row, time_from_index(row), time_from_index(row+1)))
            for column in range(0,6):
                html_result.append("                <td  %s</td> \n" % (content[column][row]))
            html_result.append("              </tr>\n")
        html_result.append(table_outro())
        return ''.join(html_result)


def time_index(time):
    return (time.minutes - 8*60) // 30

def time_from_index(index):
    return Time(index//2 + 8, (index%2) * 30)

def color_generator():
    pallete = [ "#A8FFFF", "#AFEEEE", "#00FFFF", "#87CEFA", "#A8D4FF", \
                "#B0C4DE", "#BAEDD3", "#7FFFD4", "#51FFA9", "#40E0D0", \
                "#D8BAED", "#ADFF2F", "#32CD32", "#00FF7F", "#F9A8FF", \
                "#FFBA51", "#FF9A00", "#FFA07A", "#F7AFB3", "#FFC0A8", \
                "#FFC0CB", "#FFD700", "#FFDEAD", "#FFECA8", "#F0E68C", \
                "#FFFFFF", "#F0FFF0", "#F0FFFF", "#F8F8FF", "#F5F5F5", \
                "#FFF5EE", "#F5F5DC", "#FFFFF0", "#FDF5E6", "#FAEBD7", \
                "#FFE4E1", "#FAF0E6"]
    for color in pallete:
        yield color

def intro(total_selected, total_combinations):
    return """\
    <script type='text/javascript'>
      var current = 1;
      var total = %i;

      function showTable(i) {
        document.getElementById('tt'+i).style.display = 'block';
      }
      function hideTable(i) {
        document.getElementById('tt'+i).style.display = 'none';
      }
      function updateLabel() {
        document.getElementById('label').innerHTML = current+'/'+total;
      }
      function goRight() {
        hideTable(current);
        current = (current+total)%%total+1;
        showTable(current);
        updateLabel();
      }
      function goLeft() {
        hideTable(current);
        current = (current+total-2)%%total+1;
        showTable(current);
        updateLabel();
      }
    </script>
    <p style='text-align: center'>
      <b>Combinations: <span id='label'></span></b><br>
      <span style='%sfont: 10px verdana'>(A mostrar os 100 horários mais compactos dum total de %i combinações)</span>
    </p>
    <table border='0'>
      <tr>
        <td style='width: 50px'> <img style='cursor: pointer;' src='left.png' onclick='goLeft()'> </td>
        <td style='width: 100%%'>
""" % (total_selected, "" if (total_selected < total_combinations) else "display:none;", total_combinations)

def table_intro(id_number):
    return """\
          <div style='display: none' id='tt%i' class='mtop15'>
            <table class='timetable' style='margin-left: auto; margin-right: auto' cellspacing='0' cellpadding='0' width='98%%'>
              <tr>
                <th>Horas/Dias</th>
                <th colspan='1' width='14%%' id='weekday0'>Segunda</th>
                <th colspan='1' width='14%%' id='weekday1'>Terça</th>
                <th colspan='1' width='14%%' id='weekday2'>Quarta</th>
                <th colspan='1' width='14%%' id='weekday3'>Quinta</th>
                <th colspan='1' width='14%%' id='weekday4'>Sexta</th>
                <th colspan='1' width='14%%' id='weekday5'>Sábado</th>
              </tr>
""" % (id_number)

def table_outro():
    return """\
            </table>
          </div>
"""

def outro():
    return """\
        </td>
        <td style='width: 50px'> <img style='cursor: pointer;' src='right.png' onclick='goRight()'> </td>
      </tr>
    </table>
    <script type='text/javascript'>
      showTable(current);
      updateLabel();
    </script>"""


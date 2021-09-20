try:
    import sys
    import urllib.request, urllib.parse, urllib.error
    from tt_parser import *
    from tt_generator import *
    from tt_prettyprinter import *


    course_id = int(sys.argv[1])
    url = urllib.parse.unquote(sys.argv[2])

    parser = HTMLCourseParser(url)
    course = parser.parse()

    html_result = "<div class='course p-2 shadow' id='coursediv" + str(course_id) + "' >"
    # html_result += "<img src='line.png' />"
    html_result += "<h6 class='mtop0 mbottom03 cnone'>%s" % (course.long_name)
    html_result += "<span class='greytxt'> (%s)</span>" % (course.name)
    html_result += "&nbsp&nbsp<span class='btn text-danger' style='cursor:default;' ><i class='fas fa-times-circle' onclick='removeCourse(coursediv" + str(course_id) + ")' style='cursor:pointer'></i></span>"
    html_result += "</h6>"
    html_result += "<input type='hidden' name='course%i' value='%s'>" \
                % (course_id, url)

    block_id = 0
    sorted_blocks = sorted(course.lesson_blocks, key=lambda x: x.category, reverse=True)

    for block in sorted_blocks:
        block_id += 1
        html_result += """<div class="form-check">"""
        html_result += "<input class='form-check-input' onclick='submitForm()' type='checkbox' name='course%itype%i' value='%s' checked>%s&nbsp;" \
                    % (course_id, block_id, block.category, block.category)
        html_result += "</div>"

    html_result += "</div>"
    print(html_result)
except Exception as e:
    print(e)



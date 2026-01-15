from django.shortcuts import render

# Create your views here.
def course_list(request):
    courses = [
        {'id': 1, 
         'level': 'Principiante', 
         'title': 'Python: Fundamentos',
         'rating': 4.5, 
         'instructor': 'John Doe',
         'instructor_image':'https://randomuser.me/api/portraits/women/68.jpg' ,
         'course_image': 'images/curso_1.jpg'
        },
        {
         'id': 2, 
         'level': 'Intermedio',
         'title': 'Django crea aplicaciones robustas',
         'rating': 4.7,
         'instructor': 'Jane Smith',
         'instructor_image':'https://randomuser.me/api/portraits/women/69.jpg',
         'course_image': 'images/curso_2.jpg',
        },
        {
         'id': 3,
         'level': 'Avanzado',
         'title': 'Django Avanzado',
         'rating': 4.8,
         'instructor': 'Carlos Rodriguez',
         'instructor_image':'https://randomuser.me/api/portraits/men/39.jpg',
         'course_image': 'images/curso_3.jpg'
        },
        {
        'id': 4,
        'level': 'Principiante',
        'title': 'Fast API Avanzado',
        'rating': 4.3,
        'instructor': 'Maria Garcia',
        'instructor_image':'https://randomuser.me/api/portraits/men/42.jpg',
        'course_image': 'images/curso_4.jpg'
        }
    ]
    context = {
        'courses': courses
    }
    return render(request, 'courses/courses.html', context)


def course_detail(request):
    course = {
        'course_title': 'Django Aplicaciones',
        'course_link': 'course_lessons',
        'course_image': 'images/curso_1.jpg',
        'info_course': {
           'lessons': 79,
           'duration': '8 horas',
           'instructor': 'Jane Smith',
        },
        'course_content': [
            {
                'id': 1,
                'name': 'Introducción a Django',
                'lessons':  [
                    {
                        'name': '¿Qué es Django?',
                        'type': 'video',
                    },
                    {
                        'name': '¿Instalación y configuración?',
                        'type': 'article',
                    },
                ]
            }
        ]
    }
    context = {
        'course': course
    }
    return render(request, 'courses/course_detail.html', context)


def course_lessons(request):
    lesson = {
        'course_title': 'Django Aplicaciones',
        'progress': 45,
        'course_content': [
            {
                'id': 1,
                'name': 'Introducción a Django',
                'total_lessons': 6,
                'complete_lessons': 3,
                'lessons':  [
                    {
                        'name': '¿Qué es Django?',
                        'type': 'video',
                    },
                    {
                        'name': '¿Instalación y configuración?',
                        'type': 'article',
                    },
                ]
            }
        ]
    }
    context = {
        'lesson': lesson
    }
    return render(request, 'courses/course_lessons.html', context)
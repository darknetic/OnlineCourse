from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from .models import Lesson, Submission


def course_details(request, course_id):
    from .models import Course
    course = get_object_or_404(Course.objects.prefetch_related("lessons"), pk=course_id)
    return render(request, "course/course_details_bootstrap.html", {"course": course})


@require_POST
def submit(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    questions = lesson.questions.prefetch_related("choices")
    total = questions.count()
    score = 0

    for question in questions:
        selected_id = request.POST.get(f"question_{question.id}")
        if selected_id and question.choices.filter(pk=selected_id, is_correct=True).exists():
            score += 1

    student_name = request.POST.get("student_name", "").strip() or "Student"
    submission = Submission.objects.create(
        lesson=lesson,
        student_name=student_name,
        score=score,
        total_questions=total,
    )
    return render(request, "course/exam_result.html", {"submission": submission})


def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    return render(request, "course/exam_result.html", {"submission": submission})

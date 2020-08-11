from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Note, ReNote
from .forms import NoteForm, ReNoteForm

# 쪽지 작성이 가능한 유저 목록
def user_list(request):
    receivers = User.objects.all
    return render(request, 'list.html', {'receivers':receivers})

# 쪽지 작성폼
def create_note(request, receiver_id):
    if request.method == "POST":
        note = NoteForm(request.POST)

        if note.is_valid():
            temp = note.save(commit=False)
            temp.sender = request.user
            temp.receiver = get_object_or_404(User, pk=receiver_id).username
            temp.send_at = timezone.datetime.now()
            temp.is_read = False
            temp.save()
            return redirect('home')

    note_form = NoteForm
    return render(request, 'message.html', {'note_form':note_form})

# 보낸 쪽지함
def send_notes(request):
    notes = Note.objects.filter(sender=request.user).exclude(scount=1)
    return render(request, 'notebox.html', {'notes':notes})

# 받은 쪽지함
def received_notes(request):
    notes = Note.objects.filter(receiver=request.user).exclude(rcount=1)
    return render(request, 'notebox.html', {'notes':notes})

# 쪽지 자세히 보기
def detail(request, note_id):
    note_detail = get_object_or_404(Note, pk=note_id)
    renote_form = ReNoteForm()

    # if request.user == note_detail.recever: sender는 외래키이고, receiver는 아니어서 그런지 이렇게 작성하면 함수가 제대로 작동 안 함.
    if request.user != note_detail.sender: # 요청한 유저와 쪽지를 보낸 사람이 다르면...   
        note_detail.is_read = True # 해당 함수가 실행되면 is_read를 True로 변경
        note_detail.save()
    return render(request, 'detail.html', {'note_detail':note_detail, 'renote_form':renote_form})

# 쪽지 삭제하기
# 쪽지를 받은 사람과 보낸 사람이 모두 삭제한 경우에만 DB에서 삭제
# scount와 rcount가 0이라는 것은 삭제를 시도하지 않았다는 의미로 scount와 rcount가 모두 1인 경우에만 삭제됨.
def delete_note(request, note_detail_id):
    note = get_object_or_404(Note, pk=note_detail_id)

    # 로그인한 유저 == 보내는 사람
    if request.user == note.sender:
        if note.scount == 0:
            note.scount = 1
            if note.rcount == 0:
                note.save()
                return redirect("send_notes")
            note.delete()
            return redirect('send_notes')

    # 로그인한 유저 == 받는 사람    
    else:
        if note.rcount == 0:
            note.rcount = 1
            if note.scount == 0:
                note.save()
                return redirect('received_notes')
            note.delete()
            return redirect('received_notes')    

# 받은 쪽지에 답장 보내기
def renote(request, note_detail_id):
    
    if request.method == "POST":
        renote_form = ReNoteForm(request.POST)

        if renote_form.is_valid():
            temp = renote_form.save(commit=False)
            temp.author = request.user
            temp.note = Note.objects.get(pk=note_detail_id)
            temp.save()
            return redirect('detail', note_detail_id)

# 상대방이 쪽지를 읽지 않은 경우, 쪽지를 수정
def update(request, note_detail_id):
    note = Note.objects.get(pk=note_detail_id)
    update_form = NoteForm(instance=note) # 수정할 글 담아오기!!

    if not note.is_read:
        if request.method == 'POST':
            update_form = NoteForm(request.POST, instance=note) # instance가 빠지면 새로운 글이 생성됨.

            if update_form.is_valid():
                update_form.save(commit=False)
                update_form.send_at = timezone.datetime.now()
                update_form.save()
                return redirect('detail', note_detail_id)
    else:
        pass # 경고창 띄우는 법 생각해보기.. 지금은 모르겠다.
    return render(request, 'message.html', {'note_form':update_form})

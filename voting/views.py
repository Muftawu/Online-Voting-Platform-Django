from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Position, Candidate, Vote
from django.contrib import messages


@login_required(login_url='login/')
def vote(request):
    user = request.user
    voter = user.voter 

    positions = Position.objects.all()
    key_positions = []
    candidate = ''
    selected_candidates = []

    # Verify if voter has already voted
    if voter.voted:
        messages.error(request, 'You have already voted')
        return redirect(reverse('voting:voter_dashboard'))

    # Make our post request into a dictonary
    if request.method == "POST":
        form = dict(request.POST)
        form.pop('csrfmiddlewaretoken', None)
        form.pop('submit_vote', None)

        # Ensure all required candidates are selected
        if len(form.keys()) < positions.count():
            messages.error(request, 'Please select one option from each category')
            return redirect('/')

        for key, value in form.items():
                key_positions.append(key)
        print(key_positions)
        print('------------------------------')
        
        for i, position in enumerate(positions):
            candidate = Candidate.objects.get(id=request.POST[key_positions[i]])
            candidate.polls += 1

            # Save voters choices
            vote = Vote()
            vote.position = position
            vote.candidate = candidate
            vote.voter = voter 
            vote.save()
            candidate.save()
            
            print(f'{key_positions[i]}:',  candidate)

        # Save voter status
        voter.voted = True 
        voter.save()

        messages.success(request, 'Your vote has been recorded successfully.')
        return redirect(reverse('voting:voter_dashboard'))

    context = {'positions': positions, 'selected_candidates':selected_candidates}
    return render(request, 'vote.html', context)


@login_required()
def voter_dashboard(request):
    user = request.user
    my_votes = Vote.objects.filter(voter=user.voter).all()
    context = {'my_votes': my_votes}
    return render(request, 'voter_dashboard.html', context)
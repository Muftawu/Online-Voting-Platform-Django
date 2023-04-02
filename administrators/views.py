from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from voting.models import * 

@login_required(login_url='login/')
def admin_dashboard(request):

    voters = Voter.objects.all()
    voted_voters = Voter.objects.filter(voted=True).all()

    positions = Position.objects.all()
    candidates = Candidate.objects.all()
    votes = Vote.objects.all()

    voted_voters = voters.filter(voted=True)

    position_list = []

    for position in positions:
        position_list.append(position)

    presidential_candidate = position_list[0]
    financial_candidates = position_list[1]
    women_commissioner_candidates = position_list[2]

    context = { 
            # Data 
            'voters': voters,
            'positions': positions,
            'candidates': candidates,
            'votes': votes,

            # Numbers
            'voters_total': voters.count(),
            'position_total': positions.count(),
            'candidate_total': candidates.count(),
            'votes_total': votes.count(),
            'voted_voters_total': voted_voters.count(),

            # graph data 
            'position_list': position_list,
            'presidential_candidates': presidential_candidate,
            'financial_candidates': financial_candidates,
            'women_commissioner_candidates': women_commissioner_candidates,


            }
    return render(request, 'admin_dashboard.html', context)


@login_required(login_url='login/')
def adminPositionsView(request):
    positions = Position.objects.all()
    context = {'positions': positions}
    return render(request, 'adminPositionsView.html', context)


@login_required(login_url='login/')
def adminCandidatesView(request):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates}
    return render(request, 'adminCandidatesView.html', context)


@login_required(login_url='login/')
def adminVotersView(request):
    voters = Voter.objects.all()
    context = {'voters': voters}
    return render(request, 'adminVotersView.html', context)


@login_required(login_url='login/')
def adminVotedVotersView(request):
    voted_voters = Voter.objects.filter(voted=True)
    context = {'voted_voters': voted_voters}
    return render(request, 'adminVotedVotersView.html', context)



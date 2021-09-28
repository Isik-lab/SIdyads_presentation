# SIdyads_presentation
 Presenting the dyad videos stimuli for the fMRI experiment

## SIdyads.m 
Main presentation script used for the fMRI experiment. 50 3-second dyadic videos are shown in a run. The experiment is setup with a 1.5 second TR. There is one TR black screen between most videos. On a random 10 trials, there is an additional single TR break. The final trials has an additional 9 TRs to allow for recording of the full hemodynamic response. 

The partcipant's task is to hit a button when there is a more than 2 people present in a video. These videos are not analyzed and serve as an attention control.

The script calls `write_event_files.m' to save the data in BIDS format. 

## assign_conditions.py
This must be run prior to the experiment. It can be be called by `python3 assign_conditions.py SID' where SID is the participant number. 

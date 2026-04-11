# cisc121project

## TA Grading Queue Organizer
### Merge Sort Demo  
The problem I chose for this project is a playlist vibe builder that sorts a playlist of songs based on their energy level. I chose to implement this using quick sort, as playlists are usually a small collection of songs and quick sort has a lower memory usage than merge sort. It allows for a faster average performance, as long as I choose a good pivot value.

### Test Demo
(insert demo picture here)

### Required Preconditions
For the preconditions, a random pivot index will be chosen for the general algorithm of the quick sort I will be implementing. As long as there is a list of songs with associated "energy values" for each song, quick sort will work for the playlist builder. To ensure that each song has an energy value, I will run a check using assert that ensures every song has an integer value representing its energy level.

### What To Expect For the Simulation
During the simulation, you will see the full list of songs alongside their associated energy value. At this point, a random index will be chosen to be allocated as a pivot value for the simulation. When the user presses "Sort My Playlist", the simulation will take you through a step by step process of the quick sort. Every song will be compared to the pivot value and be placed on the left/right sides accordingly and split into smaller sublists where pivots will be chosen. These sublists are recursively sorted until they are a length of 1 or 0. The final sorted playlist will be displayed on the bottom.

---

## Problem Breakdown

### Decomposition
Breaking down the problem into smaller parts, the playlist must be taken in as an input, each song having an associated integer value for the energy level. Then, implement the quick sort algorithm that recursively sorts sublists on the left and right of the pivot value, which is randomly chosen.

### Pattern Recognition
Because quick sort uses recursion, there is repeated partitioning wherein the values on the left and right of the chosen pivot values are repeatedly compared and partitioned until the entire list is sorted. The base case would be when the sublists are of size 0 or 1. 

### Abstraction
Things like the song name, lyrics, and song duration are irrelevant when making the actual algorithm to sort the playlist.

### Algorithmic Thinking
For this problem, the algorithm will first have to take an input of a playlist where each song has a specified energy level integer value. The pivot will also be chosen at this point at a random index. Then to implement the quick sort algorithm, each song will be compared to the pivot value and placed into "left/right" sublists that will also be sorted recursively until it reached a size of 0 or 1. The output should be the final sorted playlist.

### Flowchart
(insert flowchart here)

---

### Steps to Run
(Insert steps here)

---

### HuggingFace Link

---

### Author and AI Acknowledgment
By Kristina Vela   
AI Disclaimer: I did not use AI for any part of this project.

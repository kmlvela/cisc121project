# cisc121project

## TA Grading Queue Organizer
### Merge Sort Demo  
The problem I chose for this project is a TA grading queue. The app will create an ordered queue based on submission time that TA's can use to grade according to which students submit first.
I chose to implement it using merge sort. Merge sort is a stable sort, meaning the submissions will retain their relative order if two users submit at the same time. For something like a grading queue, order of submission is especially important, so a stable sort should be used to maintain this first in, first out order.

### Test Demo
(insert demo picture here)

### Required Preconditions
As for required predictions for the data, each submission should have an associated time stamp so that it can be sorted by time of submission. The stability of the merge sort must also hold to maintain fairness in the FIFO order. To enforce these predictions, the app must check if the data has comparable time stamps that all follow the same format (for example, hour : minute : second) before sorting.

### What To Expect For the Simulation
During the simulation, the user will see the list of submissions. This list will split in half and sort itself within these halved sublists until it trivially sorts itself. The sublists are then merged until the final list is sorted. 

---

## Problem Breakdown

### Decomposition
Breaking down the problem, the app will have to take a user input where assignments are submitted into a queue with an associated student ID, file name, and time stamp. Each time a new submission is received, it must be placed into its correct position into an ordered queue of assignments. The output will be a sorted list of assignments by time stamps so that the TA can grade accordingly based on what assignments were submitted first.

### Pattern Recognition
The queue will remain almost sorted each time as the submissions are taken in one at a time. The merge sort pattern makes it so that the animation will display a repeating pattern of split, then merge.

### Abstraction
For the actual sorting algorithm, details like who the student is, what the assignment is about, and who the TA is are all irrelevant to the actual problem.

### Algorithmic Thinking
The app will first validate that the dataset all have timestamps in the required format. Then, have the user make a submission. This submission is then placed into queue which will follow the merge sort algorithm: split the list into halves and recursively sort the halves until the halves are merged together into a final sorted list. The animation should highlight the new submission in its new, correct position.

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

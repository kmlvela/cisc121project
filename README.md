# cisc121project

## TA Grading Queue Organizer
### Merge Sort Demo  
The problem I chose for this project is a playlist vibe builder that sorts a playlist of songs based on their energy level. I chose to implement this using quick sort, as playlists are usually a small collection of songs and quick sort has a lower memory usage than merge sort. It allows for a faster average performance, as long as I choose a good pivot value.

### Test Demo
https://github.com/user-attachments/assets/f96cd6e1-0215-4bfa-bb0a-d59934bb5b98

### Required Preconditions
For the preconditions, a random pivot index will be chosen for the general algorithm of the quick sort I will be implementing. As long as there is a list of songs with associated "energy values" for each song, quick sort will work for the playlist builder. To ensure that each song has an associated energy level, I will create a list of dictionaries where each song will have a key for energy level and an associated integer value for each song.

### What To Expect For the Simulation
In the simulation, you will see instructions at the top of the screen to run the simulation. You may choose to randomize energy level values. Then, press 'Start Simulation' to start a step-by-step walkthough of the quick sort algorithm. You can traverse through the steps using the 'Next Step' and 'Previous Step' buttons located at the bottom. On the right side, you will see the final sorted list.

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
<img width="526" height="296" alt="Flowchart for Quick Sort" src="https://github.com/user-attachments/assets/c22e9dde-eae4-40fc-9442-60058c7ca5ed" />

---

### Steps to Run
1. Open the Hugging Face link
2. You may choose to check off the checkbox to randomize energy levels. Leaving unchecked will use default values
3. Press 'Start Simulation'
4. Use 'Next Step' and 'Previous Step' to walk you through the quick sort process
5. Once the end of the simulation is reached, you may choose to check/uncheck the randomizer or press 'Start Simulation' again to choose a different pivot

---

### HuggingFace Link
https://huggingface.co/spaces/kmlvela/CISC121-Final-Project

### Testing and Edge Cases
When testing the program, I would try the default energy level values as well as a few runthroughs of randomizing the energy levels. I also ensured that the next/previous step buttons functioned correctly. 

**Edge Case #1:** Pressing 'Next/Previous Step' before starting simulation
Before implementing a fix, the app would display the following.
<img width="949" height="408" alt="Error 1" src="https://github.com/user-attachments/assets/eb797870-9449-42dd-b05e-eb15bd5c0c7a" />

To fix this, I implemented a few lines of code in the simulation logic to check if the 'steps' list is empty or not, to which it would then display an error if it was. The following is what the app displays after this edge case handling was implemented.
<img width="941" height="409" alt="Fix 1" src="https://github.com/user-attachments/assets/ad2920f0-e8f5-4bb4-ba2e-4abd415e0ed1" />

**Edge Case #2:** 
In the event that the randomizer gives all the songs the same energy value, the simulation would run regardless as shown in the following image.
<img width="938" height="409" alt="Error 2" src="https://github.com/user-attachments/assets/9d7e7466-48bf-4bd9-b2d1-624f3e0c575b" />

To fix this, I implemented a few lines of code under the start simulation button logic that checks if all the songs have the same energy value. If so, the quick sort algorithm will exit early and tell the user that all songs are placed in the equal sublist. 
<img width="958" height="412" alt="Fix 2" src="https://github.com/user-attachments/assets/b2774435-05bf-445d-a0f0-327285d55484" />

---

### Author and AI Acknowledgment
By Kristina Vela   
AI Disclaimer: I did not use AI for any part of this project.
For all UI, I used the [gradio](https://www.gradio.app/docs/gradio/interface) website to learn how to use it.

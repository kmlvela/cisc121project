import gradio as gr
import random

# Predetermined playlist data, energy values may be randomized by the user
PREDETERMINED_PLAYLIST = [
    {"title": "SWIM", "artist": "BTS", "energy": 71},
    {"title": "Babydoll", "artist": "Dominic Fike", "energy": 60},
    {"title": "Risk It All", "artist": "Bruno Mars", "energy": 35},
    {"title": "Stateside + Zara Larsson", "artist": "PinkPantheress", "energy": 66},
    {"title": "Raindance (feat. Tems)", "artist": "Dave", "energy": 74},
    {"title": "End of Beginning", "artist": "Djo", "energy": 45},
    {"title": "Man I Need", "artist": "Olivia Dean", "energy": 59},
    {"title": "Dracula - JENNIE Remix", "artist": "Tame Impala", "energy": 79},
    {"title": "So Easy (To Fall In Love)", "artist": "Olivia Dean", "energy": 63},
    {"title": "DtMF", "artist": "Bad Bunny", "energy": 13},
]

# Format lists for clearer display of sublists less, equal, greater
def format_group(label, arr, indent):
    # Formats a list as - Title (Energy) by Artist for every song
    if not arr:
        return f"{indent}{label}: (empty)"
    lines = [f"{indent}{label}:"]
    for s in arr:
        lines.append(f"{indent} - {s['title']} ({s['energy']}) by ({s['artist']})")
    return "\n".join(lines)

# Quicksort algorithm, records every step for simulation walkthrough
def quicksort_with_steps(songs, key):
    steps = []

    # Recursive quick sort function
    def quick_sort(arr, depth = 0):
        # Makes recursion depth easy to visualize using symbols
        indent = "🌱" * depth

        # Base case for recursion, when list is empty or has 1 element
        if len(arr) <= 1:
            steps.append(
                f"{indent}Base case reached, sublist has 0 or 1 song.\n"
                f"{format_group('Group Contents', arr, indent)}\n"
            )
            return arr
        
        # Randomly chooses an index in the list to pivot around
        pivot = random.choice(arr) # Stores entire song object
        pivot_value = key(pivot) # Numeric value for comparison

        steps.append(
            f"{indent}Choosing a 'pivot' song to compare other songs against...\n"
            f"{indent}Pivot: {pivot['title']} ({pivot['energy']}) by {pivot['artist']}\n"
        )

        # Sublists for partitioning
        less, equal, greater = [], [], []

        # Sorts the songs in the array as less than, equal to, or greater than pivot
        for song in arr:
            value = key(song)
            if value < pivot_value:
                less.append(song)
                steps.append(f"{indent}{song['title']} ({value}) by {song['artist']} added to 'less energtic' sublist")
            elif value > pivot_value:
                greater.append(song)
                steps.append(f"{indent}{song['title']} ({value}) by {song['artist']} added to 'more energetic' sublist")
            else:
                equal.append(song)
                steps.append(f"{indent}{song['title']} ({value}) by {song['artist']} added to 'equal energy' sublist")

        # Display sublist groupings for user 
        steps.append(format_group("Less Energy", less, indent))
        steps.append(format_group("Equal Energy", equal, indent))
        steps.append(format_group("More Energy", greater, indent) + "\n")

        # Recursive sorting step
        steps.append(f"{indent}Sorting the less energetic group...\n")
        sorted_left = quick_sort(less, depth + 1)
        steps.append(f"{indent}Sorting the more energetic group...\n")
        sorted_right = quick_sort(greater, depth + 1)

        # Combine final results
        result = sorted_left + equal + sorted_right
        steps.append(
            f"{indent}Finished sorting!\n"
            f"{format_group('Merged Result', result, indent)}\n"
        )
        return result
    
    sorted_songs = quick_sort(songs)
    # Lets user know that simulation is completely sorted
    steps.append("Simulation complete! All songs are fully sorted\n"
                + "Press start simulation to rerun the simulation with another random pivot value. You may also choose to rerun with randomized energy levels.")
    return sorted_songs, steps

# Randomize energy levels for each song in playlist
def randomize_energy():
    return [
        {**song, "energy": random.randint(1, 100)}
        for song in PREDETERMINED_PLAYLIST
    ]

# Simulation Logic
# What to run when user presses 'Start Simulation'
def start_simulation(randomize):
    # Randomizes energy values if selected, otherwise keeps original values
    playlist = randomize_energy() if randomize else PREDETERMINED_PLAYLIST.copy()

    # In case all energies are equal, no sorting is needed
    energies = [s["energy"] for s in playlist]
    # Set will be length 1 since it allows for no duplicates
    if len(set(energies)) == 1:
        steps = ["All songs have the same energy level!\nThe quick sort algorithm stops here as all values belong to the 'equal' sublist.",]
        final_result =  "\n".join(
            f"- {s['title']} ({s['energy']}) by {s['artist']}"
            for s in playlist
        )
        return steps, 0, steps[0], final_result

    # Average case, run quick sort simulation
    sorted_songs, steps = quicksort_with_steps(playlist, key = lambda s: s["energy"])
    current_index = 0
    current_view = steps[current_index]

    final_result = "\n".join(
    f"- {s['title']} ({s['energy']}) by {s['artist']}" 
    for s in sorted_songs
    )

    return steps, current_index, current_view, final_result

# What to run when user presses 'Next Step'
def next_step(steps, current_index):
    # Handles edge cases/error if user presses next step before starting simulation
    if not steps:
        return steps, current_index, "⚠️ Please start the simulation first!"
    current_index = min(current_index + 1, len(steps) - 1)
    return steps, current_index, steps[current_index]

# What to run when user presses 'Previous Step'
def prev_step(steps, current_index):
        # Handles edge cases/error if user presses previous step before starting simulation
    if not steps:
        return steps, current_index, "⚠️ Please start the simulation first!"
    current_index = max(current_index - 1, 0)
    return steps, current_index, steps[current_index]

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 🎵 Playlist Vibe Builder - Quick Sort Demo")
    gr.Markdown("#### This simulation sorts a predetermined playlist of songs based on their associated energy level\n"
                + "Press 'start simulation' to begin and 'next step' or 'previous step' to walk you through the quick sort process! You may also choose to randomize the energy levels of each song.")
    gr.Markdown("Recursion depth is marked with the 🌱 symbol")
    gr.Markdown("Playlist sourced from the Spotify Top 50 Global Chart as of April 10, 2026")

    randomize_checkbox = gr.Checkbox(label="Randomize energy levels?", value = False)

    with gr.Row():
        # Left column for walkthrough
        with gr.Column(scale=2):
            step_display = gr.Textbox(label="Current Step", lines = 22, interactive = False)

            with gr.Row():
                start_btn = gr.Button("Start Simulation")
                prev_btn = gr.Button("Previous Step")
                next_btn = gr.Button("Next Step")

        # Right column to display sorted playlist
        with gr.Column(scale=1):
            final_result_display = gr.Textbox(
                label = "Final Sorted Playlist",
                lines = 22,
                interactive = False
            )
    
    # Internal state for steps and index
    steps_state = gr.State([])
    index_state = gr.State(0)

    # Button actions
    start_btn.click(
        start_simulation, 
        inputs = [randomize_checkbox], 
        outputs = [steps_state, index_state, step_display, final_result_display]
    )

    next_btn.click(
        next_step, 
        inputs=[steps_state, index_state], 
        outputs = [steps_state, index_state, step_display]
    )

    prev_btn.click(
        prev_step, 
        inputs = [steps_state, index_state], 
        outputs = [steps_state, index_state, step_display]
    )

demo.launch()
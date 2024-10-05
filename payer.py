import pyautogui
import time

# Coordinates
stash_coords = (550, 269)  # Initial stash coordinates to retrieve chaos orbs
inventory_coords = (1288, 609)  # Stash coordinates to return remaining chaos orbs


def transfer_exact_chaos_orbs(n):
    # Step 1: Ctrl+Click to retrieve chaos orbs until we have at least n in inventory
    collected_orbs = 0
    while collected_orbs < n:
        pyautogui.moveTo(stash_coords[0], stash_coords[1])
        pyautogui.keyDown('ctrl')
        pyautogui.click()  # Ctrl+Click to take a stack
        pyautogui.keyUp('ctrl')

        collected_orbs += 20  # Assuming each stack is 20, adjust if different
        time.sleep(0.2)  # Small delay to mimic human behavior

    # Step 2: Hold shift and click to place exactly n chaos orbs in inventory
    pyautogui.moveTo(inventory_coords[0], inventory_coords[1])
    pyautogui.click()
    pyautogui.keyDown('shift')
    for _ in range(n % 20):
        pyautogui.click()
        time.sleep(0.1)  # Small delay between each click
    pyautogui.keyUp('shift')

    # Step 3: Move to the inventory and put back the remaining orbs in the stash
    pyautogui.moveTo(stash_coords[0], stash_coords[1])
    pyautogui.click()  # Click to return remaining chaos orbs to the stash

    # Optional: Slight delay before ending the script
    time.sleep(0.5)


# Number of chaos orbs you want to transfer
n = 7

# Run the transfer
transfer_exact_chaos_orbs(n)

def close_multiple_windows(chrome):
    all_tab_list=chrome.window_handles
    current_tab=chrome.current_window_handle

    for window in all_tab_list:
        if window!=current_tab:
            chrome.switch_to.window(window)
            chrome.close()

    chrome.switch_to.window(current_tab)
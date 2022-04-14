import thelittlethings.progress_bar as progress_bar

if __name__ == '__main__':
    iterations = 100_000
    # Create a progress bar
    bar = progress_bar.ProgressBar(max_value=iterations)
    # Iterably approximate pi
    k = 1
    pi = 0    
    for i in range(iterations):
        if i % 2 == 0:
            pi += 4/k
        else:
            pi -= 4/k
        k += 2
        # Update the progress bar (bar.progress = i | bar.update(i))
        bar.progress = i

    bar.finish()
    print(f"Pi is approximately {pi}")
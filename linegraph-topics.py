import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# removes columns withtout consistently written articles
def formatData():
    data = pd.read_csv('updated_stats1.csv')
    sectionNames = data.columns.values
    for name in sectionNames:
        col = data[name]
        if col.isnull().values.any():
            data = data.drop(name, axis=1)
    return data

# creates line graphs
def makeLineGraphs(gender_category_data):

    # These are the "Tableau 20" colors as RGB.
    tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
                 (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
                 (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
                 (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
                 (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
                 (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
                 (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
                 (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
                 (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
    for i in range(len(tableau20)):
        r, g, b = tableau20[i]
        tableau20[i] = (r / 255., g / 255., b / 255.)

    # You typically want your plot to be ~1.33x wider than tall. This plot is a rare
    # exception because of the number of lines being plotted on it.
    # Common sizes: (10, 7.5) and (12, 9)
    plt.figure(figsize=(16, 12))

    # Remove the plot frame lines. They are unnecessary chartjunk.
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    # Ensure that the axis ticks only show up on the bottom and left of the plot.
    # Ticks on the right and top of the plot are generally unnecessary chartjunk.
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    # Limit the range of the plot to only where the data is.
    # Avoid unnecessary whitespace.
    plt.ylim(0, 86)
    plt.xlim(1, 73)
    #NOTE: FIGURE OUT X AXIS

    # Make sure your axis ticks are large enough to be easily read.
    # You don't want your viewers squinting to read your plot.
    plt.yticks(range(0, 86, 10), [str(x) + "%" for x in range(0, 73, 10)], fontsize=14)
    plt.xticks(fontsize=14)

    # Provide tick lines across the plot to help your viewers trace along
    # the axis ticks. Make sure that the lines are light and small so they
    # don't obscure the primary data lines.
    for y in range(10, 91, 10):
        plt.plot(range(1, 73), [y] * len(range(1, 73)), "--", lw=0.5, color="black", alpha=0.3)

    # Remove the tick marks; they are unnecessary with the tick lines we just plotted.
    plt.tick_params(axis="both", which="both", bottom="off", top="off",
                    labelbottom="on", left="off", right="off", labelleft="on")

    # Now that the plot is prepared, it's time to actually plot the data!
    # Note that I plotted the majors in order of the highest % in the final year.
    # topics = ['Travel', 'Real Estate', 'Fashion & Style', 'Food',
    #           'N.Y. / Region', 'Health', 'Arts', 'Magazine', 'Books',
    #           'Business', 'Multimedia', 'Movies', 'World', 'Science',
    #           'U.S.', 'Your Money', 'Opinion', 'Theater', 'Technology',
    #           'Sports', 'Automobiles', 'Crosswords & Games', 'Job Market']
    topics = ['Travel', 'Fashion & Style',
              'Books', 'Business', 'Multimedia',
              'Movies', 'World', 'U.S.', 'Theater',
              'Technology', 'Sports']

    for rank, column in enumerate(topics):
        # Plot each line separately with its own color, using the Tableau 20
        # color set in order.
        plt.plot(gender_category_data.Month.values,
                gender_category_data[column.replace("\n", " ")].values,
                lw=2.5, color=tableau20[rank])

        # Add a text label to the right end of every line. Most of the code below
        # is adding specific offsets y position because some labels overlapped.
        y_pos = gender_category_data[column.replace("\n", " ")].values[-1] - 0.5
        if column == "Travel":
            y_pos += 0.5
        elif column == "Fashion &\nStyle":
            y_pos -= 0.5
        elif column == "Books":
            y_pos += 1
        elif column == "Business":
            y_pos += 0.5
        elif column == "Multimedia":
            y_pos -= 0.5
        elif column == "Movies":
            y_pos -= 1.75
        elif column == "World":
            y_pos += 0.25
        elif column == "U.S.":
            y_pos -= 0.75
        elif column == "Theater":
            y_pos -= 0.5
        elif column == "Technology":
            y_pos += 1
        elif column == "Sports":
            y_pos -= 0.5

        # Again, make sure that all labels are large enough to be easily read
        # by the viewer.
        plt.text(73, y_pos, column, fontsize=14, color=tableau20[rank])

    # matplotlib's title() call centers the title on the plot, but not the graph,
    # so I used the text() call to customize where the title goes.

    # Make the title big enough so it spans the entire plot, but don't make it
    # so big that it requires two lines to show.

    plt.savefig("percent-female-writer-topic.png", bbox_inches="tight")

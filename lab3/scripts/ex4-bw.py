import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import timedelta

labels_for_axis = {
    "summer semester": 'semesters',
    "winter semester": 'semesters',
    "winter holidays": "holidays",
    "holidays between semesters": "holidays",
    "spring holidays": "holidays",
    "summer holidays": "holidays",
    "final decisions 2024/2025": "final decisions",
    "final decisions winter semester": "final decisions",
    "cc summer 2024/2025": "cc",
    "cc 2025/2026": "cc",
    "rpc winter deadline": "rpc",
    "rpc summer deadline": "rpc",
    "classes (block I)": "classes",
    "classes (block II)": "classes",
    "classes (block III)": "classes",
    "exam session": "exams",
    "exam resit session": "exams",
    "fl exams": "exams",
    "summer holidays (block I)": "holidays",
    "summer holidays (block II)": "holidays",
    "sdr deadline": "sdr",
    "free days": "free days",
}

code_to_style = {
    "holidays": {"linestyle": "-", "linewidth": 3, "color": "0.8"},
    "exams": {"linestyle": ":", "linewidth": 4, "color": "0.7"},
    "final decisions": {"linestyle": ":", "linewidth": 3, "color": "0.5"},
    "cc": {"linestyle": "-.", "linewidth": 2, "color": "0.3"},
}

code_to_full_description = {
    "I, II, III": "blocks of classes/holidays",
    "NE": "normal session of exams",
    "RE": "resit session of exams",
    "FL": "written certification exams in foreign languages",
    "sdr": "deadline for submitting a deletion request connecting the subject to the study program",
    "rpc": "deadline for resignation from passing the course:\n       winter - in the winter semester; summer - in the summer semester",
    "cc": "the period for connecting courses taken:\n       summer 2024/2025 - in the summer semester; 2025/2026 - in the winter semester and the entire academic year 2025/2026",
    "final decisions": "the period in which all individual decisions regarding passing:\n       winter - the winter semester 2024/2025 must be made; 2024/2025 - the academic year 2024/2025 should be made",
    "free days": "free days from didactic classes",
}

labels_in_plot = {
    "summer semester": 'summer',
    "winter semester": 'winter',
    "winter holidays": "winter",
    "holidays between semesters": "between semesters",
    "spring holidays": "spring",
    "summer holidays": "summer",
    "final decisions 2024/2025": "2024/2025",
    "final decisions winter semester": "winter",
    "cc summer 2024/2025": "summer 2024/2025",
    "cc 2025/2026": "2025/2026",
    "rpc winter deadline": "winter",
    "rpc summer deadline": "summer",
    "classes (block I)": "I",
    "classes (block II)": "II",
    "classes (block III)": "III",
    "exam session": "NE",
    "exam resit session": "RE",
    "fl exams": "FL",
    "summer holidays (block I)": "I",
    "summer holidays (block II)": "II",
}

desired_order = ['semesters', 'classes', 'holidays', 'free days', 'exams', 'sdr', 'rpc', 'cc', 'final decisions']


def set_new_label(desc):
    return labels_for_axis.get(desc, desc)


def main():
    tasks = pd.read_csv("../data/ex4.csv")
    tasks['start_date'] = pd.to_datetime(tasks['start_date'], format='%d.%m.%Y')
    tasks['finish_date'] = pd.to_datetime(tasks['finish_date'], format='%d.%m.%Y', errors='coerce')

    fig, ax = plt.subplots(figsize=(16, 7))

    label_positions = {label: i for i, label in enumerate(desired_order)}

    for i, task in tasks.iterrows():
        y_position = label_positions[set_new_label(task['description'])]

        start = task['start_date']
        if pd.isnull(task['finish_date']):
            ax.plot([start, start], [y_position - 0.1, y_position + 0.1], color="black", linewidth=2)
            pos = -0.5
            loc = 'center'
            if labels_for_axis[task['description']] == 'rpc':
                txt = task['description'][4:-8]
            else:
                txt = task['start_date'].strftime('%d.%m')
                if txt == '09.05':
                    pos = 0.1
                elif txt == '10.05':
                    txt = '         10.05'

            ax.text(start, y_position + pos, txt, fontsize=12, ha=loc, va='bottom')
        else:
            finish = task['finish_date']
            middle = start + (finish - start) / 2
            try:
                style = code_to_style[labels_for_axis[task['description']]]
            except KeyError:
                style = {"linestyle": "-", "marker": None, "linewidth": 2, "color": "0.2"}

            if task['description'] == 'classes (block I)':
                style = {"linestyle": ":", "linewidth": 2, "color": "0.4"}
            elif task['description'] == 'classes (block II)':
                style = {"linestyle": "-.", "linewidth": 2, "color": "0.4"}
            elif task['description'] == 'classes (block III)':
                style = {"linestyle": "-", "linewidth": 2, "color": "0.4"}
            elif task['description'] == 'winter semester':
                style = {"linestyle": "--", "linewidth": 4, "color": "0.2"}
            elif task['description'] == 'summer semester':
                style = {"linestyle": "--", "linewidth": 4, "color": "0.6"}

            txt = labels_in_plot.get(task['description'], task['description'])

            if txt == 'FL':
                pos = -0.5
                txt = 'FL (' + task['start_date'].strftime('%d.%m') + ')'
            else:
                pos = 0.15

            if (txt == 'I' or txt == 'II') and labels_for_axis[task['description']] == 'holidays':
                pos = -0.5
                style = {"linestyle": "-", "linewidth": 1, "color": "1"}
                ax.plot([start, finish], [y_position, y_position], **style)
                ax.text(middle, y_position + pos, txt, fontsize=12, ha='center', va='bottom')
                continue

            ax.plot([start, finish], [y_position, y_position], **style)
            ax.text(middle, y_position + pos, txt, fontsize=12, ha='center', va='bottom')

    ax.set_yticks(range(len(desired_order)))
    ax.set_yticklabels(desired_order)
    ax.set_ylim(-0.5, len(desired_order) - 0.5)

    ax.xaxis.set_major_locator(mdates.WeekdayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m'))
    descriptions_text = "Legend:\n" + "\n".join([f"{code} - {desc}" for code, desc in code_to_full_description.items()])
    plt.figtext(0.05, -0.3, descriptions_text, ha="left", fontsize=10, wrap=True)

    plt.annotate('', xy=(0.01, -0.12), xycoords='axes fraction', xytext=(0.09, -0.12),
                 textcoords='axes fraction', arrowprops=dict(arrowstyle="-", color="black"))
    plt.annotate('OCTOBER', xy=(0.045, -0.15), xycoords='axes fraction', textcoords='axes fraction', ha='center', va='bottom', fontsize=10)

    plt.annotate('', xy=(0.092, -0.12), xycoords='axes fraction', xytext=(0.17, -0.12),
                 textcoords='axes fraction', arrowprops=dict(arrowstyle="-", color="black"))
    plt.annotate('NOVEMBER', xy=(0.13, -0.15), xycoords='axes fraction', textcoords='axes fraction', ha='center', va='bottom', fontsize=10)

    plt.annotate('', xy=(0.172, -0.12), xycoords='axes fraction', xytext=(0.26, -0.12),
                 textcoords='axes fraction', arrowprops=dict(arrowstyle="-", color="black"))
    plt.annotate('DECEMBER', xy=(0.215, -0.15), xycoords='axes fraction', textcoords='axes fraction', ha='center', va='bottom', fontsize=10)

    plt.annotate('', xy=(0.262, -0.12), xycoords='axes fraction', xytext=(0.335, -0.12),
                 textcoords='axes fraction', arrowprops=dict(arrowstyle="-", color="black"))
    plt.annotate('JANUARY', xy=(0.3, -0.15), xycoords='axes fraction', textcoords='axes fraction', ha='center', va='bottom', fontsize=10)

    plt.annotate('', xy=(0.337, -0.12), xycoords='axes fraction', xytext=(0.41, -0.12),
                 textcoords='axes fraction', arrowprops=dict(arrowstyle="-", color="black"))
    plt.annotate('FEBRUARY', xy=(0.376, -0.15), xycoords='axes fraction', textcoords='axes fraction', ha='center', va='bottom', fontsize=10)

    plt.annotate('', xy=(0.412, -0.12), xycoords='axes fraction', xytext=(0.49, -0.12),
                 textcoords='axes fraction', arrowprops=dict(arrowstyle="-", color="black"))
    plt.annotate('MARCH', xy=(0.45, -0.15), xycoords='axes fraction', textcoords='axes fraction', ha='center', va='bottom', fontsize=10)

    plt.annotate('', xy=(0.492, -0.12), xycoords='axes fraction', xytext=(0.58, -0.12),
                 textcoords='axes fraction', arrowprops=dict(arrowstyle="-", color="black"))
    plt.annotate('APRIL', xy=(0.535, -0.15), xycoords='axes fraction', textcoords='axes fraction', ha='center', va='bottom', fontsize=10)

    plt.annotate('', xy=(0.582, -0.12), xycoords='axes fraction', xytext=(0.66, -0.12),
                 textcoords='axes fraction', arrowprops=dict(arrowstyle="-", color="black"))
    plt.annotate('MAY', xy=(0.62, -0.15), xycoords='axes fraction', textcoords='axes fraction', ha='center', va='bottom', fontsize=10)

    plt.annotate('', xy=(0.662, -0.12), xycoords='axes fraction', xytext=(0.74, -0.12),
                 textcoords='axes fraction', arrowprops=dict(arrowstyle="-", color="black"))
    plt.annotate('JUNE', xy=(0.7, -0.15), xycoords='axes fraction', textcoords='axes fraction', ha='center', va='bottom', fontsize=10)

    plt.annotate('', xy=(0.742, -0.12), xycoords='axes fraction', xytext=(0.825, -0.12),
                 textcoords='axes fraction', arrowprops=dict(arrowstyle="-", color="black"))
    plt.annotate('JULY', xy=(0.78, -0.15), xycoords='axes fraction', textcoords='axes fraction', ha='center', va='bottom', fontsize=10)

    plt.annotate('', xy=(0.827, -0.12), xycoords='axes fraction', xytext=(0.9, -0.12),
                 textcoords='axes fraction', arrowprops=dict(arrowstyle="-", color="black"))
    plt.annotate('AUGUST', xy=(0.865, -0.15), xycoords='axes fraction', textcoords='axes fraction', ha='center', va='bottom', fontsize=10)

    plt.annotate('', xy=(0.902, -0.12), xycoords='axes fraction', xytext=(0.99, -0.12),
                 textcoords='axes fraction', arrowprops=dict(arrowstyle="-", color="black"))
    plt.annotate('SEPTEMBER', xy=(0.95, -0.15), xycoords='axes fraction', textcoords='axes fraction', ha='center', va='bottom', fontsize=10)

    plt.xticks(rotation=45)
    plt.yticks(fontsize=12)
    plt.title('Calendar of the Next Academic Year (2024/2025)', fontsize=16)
    plt.xlim(tasks['start_date'].min() - timedelta(days=5), tasks['finish_date'].max() + timedelta(days=5))
    plt.tight_layout()
    plt.grid(True, ls='--', lw=.5, c='k', alpha=0.6)

    fig.savefig("../plots/ex4-b&w.pdf", bbox_inches='tight')


if __name__ == '__main__':
    main()

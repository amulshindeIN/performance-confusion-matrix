import numpy as np

def performanceConfusionMatrix(confusion_matrix = [], sel_class = 0):
    """
    pass the confusion matrix(cm), and select the desired integer class (class).
    This function will provide TP, FP, FN, and TN values.
    """
    # sel = 2
    sel = sel_class
    cm = confusion_matrix

    row_columns = list(np.arange(len(cm)))
    row_columns.remove(sel)
    row_columns

    # True Positive
    TP = cm[sel][sel]

    # False Positive
    FP=0
    for i in row_columns:
        FP += cm[sel][i]

    # False Negative
    FN = 0
    for i in row_columns:
        FN += cm[i][sel]

    # True Negative
    TN=0
    for i in row_columns:
        for j in row_columns:
            TN += cm[i][j]

    return TP, FP, FN, TN

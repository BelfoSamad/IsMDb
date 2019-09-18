from __future__ import print_function

from numpy import trapz
import numpy as np
import pandas as pd
from IsMDb.utils import convert_to_dataframe


# get slope of line given 2 points
def get_slope(A=(0, 0), B=(0, 0)):
    return (B[1] - A[1]) / (B[0] - A[0])


# get y-intercept of line given 2 a point and the slope
def get_y_intercept(A=(0, 0), slope=1):
    b = A[1] - slope * A[0]
    return b


# get intersection points
def get_intersection_points(f1, f2, step=1):
    inters_points = []
    # declare variables which will be used to iterate over the list of points for each function
    # knowing that both lists f1 and f2 are of the same size
    size = len(f1)
    # Xn-1 :
    i = 0
    # Xn :
    j = 1

    while j < size:
        # if f1[i] == f1[j] and f2[i] == f2[j]:
        #     # if (f1[i] == f2[i]):
        #         i += 1
        #         j += 1
        #         continue
        A = ((i) * step, f1[i])
        B = ((j) * step, f1[j])
        C = ((i) * step, f2[i])
        D = ((j) * step, f2[j])

        # find slopes of each segment
        slope_seg1 = get_slope(A, B)
        slope_seg2 = get_slope(C, D)

        # check if the segments are parallel to each other in that case skip the iteration and go to the next one
        if slope_seg1 == slope_seg2:
            i += 1
            j += 1
            continue
        # find y-intercept of each segment
        y_itcpt_seg1 = get_y_intercept(A, slope_seg1)
        y_itcpt_seg2 = get_y_intercept(C, slope_seg2)

        # compute intersection point let Px and Py be its coordinators
        Px = ((y_itcpt_seg2 - y_itcpt_seg1) / (slope_seg1 - slope_seg2))
        Py = slope_seg1 * Px + y_itcpt_seg1

        # check first if the point is inside the correct interval
        if (Px >= i * step) and (Px <= j * step):
            # append the point to the list of points
            intersection_point = (Px, Py)
            inters_points.append(intersection_point)

        i += 1
        j += 1

    return inters_points


def get_all_segments(f1, f2, step=1):
    intsct_pts = get_intersection_points(f1, f2, step)
    # transform f1 and f2 into enumerated list of the same elements
    # for example : [1,2,3] => [(0,1),(1,2),(2,3)]
    f1 = list(enumerate(f1))
    f2 = list(enumerate(f2))
    segments_list_f1 = []
    segments_list_f2 = []
    size = len(f1)
    i = 0
    j = 1
    intsct_pt_index = 0
    while j < size:
        seg1 = [(f1[i][0] * step, f1[i][1]), (f1[j][0] * step, f1[j][1])]
        seg2 = [(f2[i][0] * step, f2[i][1]), (f2[j][0] * step, f2[j][1])]
        if intsct_pts:
            if intsct_pt_index < len(intsct_pts):
                intsct_pt = intsct_pts[intsct_pt_index]
                intsct_pt_index += 1
                if i * step < intsct_pt[0] < j * step:
                    seg11 = [(f1[i][0] * step, f1[i][1]), (intsct_pt[0], intsct_pt[1])]
                    seg12 = [(intsct_pt[0], intsct_pt[1]), (f1[j][0] * step, f1[j][1])]
                    seg21 = [(f2[i][0] * step, f2[i][1]), (intsct_pt[0], intsct_pt[1])]
                    seg22 = [(intsct_pt[0], intsct_pt[1]), (f2[j][0] * step, f2[j][1])]
                    segments_list_f1.append(seg11)
                    segments_list_f1.append(seg12)
                    segments_list_f2.append(seg21)
                    segments_list_f2.append(seg22)
            else:
                segments_list_f1.append(seg1)
                segments_list_f2.append(seg2)
        else:
            segments_list_f1.append(seg1)
            segments_list_f2.append(seg2)
        i += 1
        j += 1

    return [segments_list_f1, segments_list_f2]


def get_integral_similarity(f1, f2, step=1):
    area_f1 = trapz(f1, dx=step)
    area_f2 = trapz(f2, dx=step)
    biggest_area = max(area_f1, area_f2)
    all_segments = get_all_segments(f1, f2, step)
    f1_segments = all_segments[0]
    f2_segments = all_segments[1]
    size = len(f1_segments)
    i = 0
    area_difference = 0
    while i < size:
        segment_area_from_f1 = trapz([f1_segments[i][0][1], f1_segments[i][1][1]],
                                     dx=f1_segments[i][1][0] - f1_segments[i][0][0])
        segment_area_from_f2 = trapz([f2_segments[i][0][1], f2_segments[i][1][1]],
                                     dx=f2_segments[i][1][0] - f2_segments[i][0][0])
        segment_area_difference = max(segment_area_from_f1,
                                      segment_area_from_f2) - min(segment_area_from_f1,
                                                                  segment_area_from_f2)
        area_difference += segment_area_difference
        i += 1
    if biggest_area != 0:
        return 1 - area_difference / biggest_area
    else:
        return 1


def get_criteria_similarity(qs, collected_reviews):
    # problem starts here , get_integral_similarity will give u similarity between 2 reviews ( by giving f1 and f2 which are
    # the criterias (lists) for review1 and review2 ((u don't need to give step a value)) , so our problem is to feed
    # that algorithm alle the reviews in f1 and in f2 as well
    # to create a big matrix which contains the similarities between all reviews to all reviews ,
    # SO we have to store the ID or some index(identifier) that tells us which review we're at ,
    # by that i mean for example full_similarity_matrix[25][2] should give
    # the similarity between review 25 and the review 2 those numbers are
    # the unique identifiers for these 2 reviews got it?
    # -------------------- you can stop here and i ll do the rest -----------------
    # and then now comes the time to use collected reviews ( liked by the member )
    # we iterate over the collected reviews using the id of each review to get the similarity list from
    # the full_similarity_matrix we get the highest similar review from each list and then randomize the new list
    # i got the code to randomize , don't bother searching , and thats it
    df = convert_to_dataframe(qs, fields=['title'])
    df_copy = convert_to_dataframe(qs, fields=['alcohol', 'nudity', 'LGBTQ', 'sex', 'language', 'violence'])

    full_similarity_matrix = []

    criteria = []
    for index, row in df_copy.iterrows():
        c = [row['alcohol'], row['nudity'], row['LGBTQ'], row['sex'], row['language'], row['violence']]
        criteria.append(c)

    rows = 0
    df['words'] = ''
    for index, row in df.iterrows():
        row['words'] = criteria[index]
        rows = rows + 1

    df = df[['title', 'words']]

    columns = df.columns
    matrix = np.zeros(shape=(rows, rows))
    i = 0
    j = 0
    for index1, row1 in df.iterrows():
        for index2, row2 in df.iterrows():
            for col in columns:
                if col == 'words':
                    print('----------------------------------')
                    print(row1[col])
                    print('----------------------------------')
                    print(row2[col])
                    matrix[i, j] = get_integral_similarity(row1[col], row2[col])
            j = j + 1
        j = 0
        i = i + 1

    print(matrix)
    print("--------------------------------------------------------------")
    print(matrix[0][0])

    # get indices
    indices = pd.Series(df['title'])

    for review in collected_reviews.all():
        idx = indices[indices == review.title].index[0]
        score_series = pd.Series(matrix[idx]).sort_values(ascending=False)
        top_10_indexes = list(score_series.iloc[1:11].index)
        for i in top_10_indexes:
            # Adding the Top 10 for every review
            full_similarity_matrix.append(list(df['title'])[i])

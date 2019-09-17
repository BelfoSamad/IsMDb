from __future__ import print_function

from numpy import trapz


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

    return 1 - area_difference / biggest_area


def get_criteria_similarity():
    pass

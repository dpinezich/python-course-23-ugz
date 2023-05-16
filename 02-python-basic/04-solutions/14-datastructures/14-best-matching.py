def best_matching(s1, s2, s3):
    matches_s1_s2 = s1 & s2
    matches_s1_s3 = s1 & s3

    n_matches_s1_s2 = len(matches_s1_s2)
    n_matches_s1_s3 = len(matches_s1_s3)

    if n_matches_s1_s2 > n_matches_s1_s3:
        return "s2"
    else:
        return "s3"


print(best_matching(s1=set('abc'), s2=set('bcde'), s3=set('bdklm')))

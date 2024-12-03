student_answer_list = {}

suggestion_list = {
    "courseList": [
        {
            "Stream": "IT",
            "Difficulty": "Easy",
            "Percentage": "30%",
            "Suggestion": [
                {
                    "CourseName": "Java", 
                    "CourseLink": "https://www.w3schools.com/java/",
                    "CourseVideoLink": "https://www.youtube.com/watch?v=A74TOX803D0"
                },
                {
                    "CourseName": "Python",
                    "CourseLink": "https://www.geeksforgeeks.org/python-ways-to-find-length-of-list/",
                    "CourseVideoLink": "https://www.youtube.com/watch?v=XKHEtdqhLK8"
                }
            ]
        },
        {
            "Stream": "IT",
            "Difficulty": "Easy",
            "Percentage": "60%",
            "Suggestion": [
                {
                    "CourseName": "Javascript",
                    "CourseLink": "https://www.w3schools.com/js/js_syntax.asp",
                    "CourseVideoLink": "https://youtu.be/lfmg-EJ8gm4?si=WcV1IKKA6Ev9ryv_"
                },
                {
                    "CourseName": "C",
                    "CourseLink": "https://www.tutorialspoint.com/cprogramming/c_overview.htm",
                    "CourseVideoLink": "https://youtu.be/KJgsSFOSQv0?si=b4Q0SsItgVCQqWXi"
                }
            ]
        },
        {
            "Stream": "IT",
            "Difficulty": "Easy",
            "Percentage": "90%",
            "Suggestion": [
                {
                    "CourseName": "C#",
                    "CourseLink": "https://www.javatpoint.com/c-sharp-tutorial",
                    "CourseVideoLink": "https://youtu.be/gfkTfcpWqAY?si=qPdBaCtmbxvJmMvm"
                },
                {
                    "CourseName": "PHP",
                    "CourseLink": "https://www.w3schools.com/php/php_intro.asp",
                    "CourseVideoLink": "https://youtu.be/OK_JCtrrv-c?si=Ca5RiZPiVHM2ScdF"
                }
            ]
        },
        {
            "Stream": "IT",
            "Difficulty": "Medium",
            "Percentage": "30%",
            "Suggestion": [
                {
                    "CourseName": "Ruby",
                    "CourseLink": "https://www.tutorialspoint.com/ruby/ruby_overview.htm",
                    "CourseVideoLink": "https://youtu.be/t_ispmWmdjY?si=YLlcFavg34sDMBkN"
                },
                {
                    "CourseName": "Go",
                    "CourseLink": "https://www.w3schools.com/go/go_introduction.php",
                    "CourseVideoLink": "https://youtu.be/yyUHQIec83I?si=scc1O2AnXDNryfdv"
                }
            ]
        },
        {
            "Stream": "IT",
            "Difficulty": "Medium",
            "Percentage": "60%",
            "Suggestion": [
                {
                    "CourseName": "Perl",
                    "CourseLink": "https://www.tutorialspoint.com/perl/perl_introduction.htm",
                    "CourseVideoLink": "https://youtu.be/WEghIXs8F6c?si=tGocPSUyTJ4caHDX"
                },
                {
                    "CourseName": "SQL",
                    "CourseLink": "https://www.w3schools.com/sql/sql_intro.asp",
                    "CourseVideoLink": "https://youtu.be/hlGoQC332VM?si=OoGvG1t3a2hoT-wo"
                }
            ]
        },
        {
            "Stream": "IT",
            "Difficulty": "Medium",
            "Percentage": "90%",
            "Suggestion": [
                {
                    "CourseName": "HTML",
                    "CourseLink": "https://www.w3schools.com/html/html5_geolocation.asp",
                    "CourseVideoLink": "https://youtu.be/HD13eq_Pmp8?si=rOhiMiWVl-GFv6KV"
                },
                {
                    "CourseName": "CSS",
                    "CourseLink": "https://www.w3schools.com/css/css_rwd_intro.asp",
                    "CourseVideoLink": "https://youtu.be/wRNinF7YQqQ?si=UsB209SOkSL0Dmhb"
                }
            ]
        },
        {
            "Stream": "IT",
            "Difficulty": "Hard",
            "Percentage": "30%",
            "Suggestion": [
                {
                    "CourseName": "Bootstrap",
                    "CourseLink": "https://www.w3schools.com/bootstrap5/bootstrap_get_started.php",
                    "CourseVideoLink": "https://youtu.be/-qfEOE4vtxE?si=WaKtynJ05KUqBMYF"
                },
                {
                    "CourseName": "NodeJs",
                    "CourseLink": "https://www.w3schools.com/nodejs/nodejs_get_started.asp",
                    "CourseVideoLink": "https://youtu.be/TlB_eWDSMt4?si=bz_84Bo_wa6s5aEN"
                }
            ]
        },
        {
            "Stream": "IT",
            "Difficulty": "Hard",
            "Percentage": "60%",
            "Suggestion": [
                {
                    "CourseName": "Express",
                    "CourseLink": "https://www.geeksforgeeks.org/express-js/",
                    "CourseVideoLink": "https://youtu.be/7H_QH9nipNs?si=-GGy2oxJpd9NMrPL"
                },
                {
                    "CourseName": "React",
                    "CourseLink": "https://www.w3schools.com/react/react_getstarted.asp",
                    "CourseVideoLink": "https://youtu.be/SqcY0GlETPk?si=HCE7ecZk3eNf-AbD"
                }
            ]
        },
        {
            "Stream": "IT",
            "Difficulty": "Hard",
            "Percentage": "90%",
            "Suggestion": [
                {
                    "CourseName": "MERN",
                    "CourseLink": "https://www.geeksforgeeks.org/mern-stack/",
                    "CourseVideoLink": "https://youtu.be/ORyi6tTMNqE?si=f9aICh0WN9uUaDOy"
                },
                {
                    "CourseName": "MEAN",
                    "CourseLink": "https://www.geeksforgeeks.org/introduction-to-mean-stack/",
                    "CourseVideoLink": "https://youtu.be/48SUuk8e55c?si=2aVcZldjJoVpqT70"
                }
            ]
        }
    ]
}

def get_suggestions(student_answer_list, suggestion_list):
    easy_score = 0
    medium_score = 0
    hard_score = 0
    
    if student_answer_list['easy']['total_question']!=0:
        easy_score = (student_answer_list['easy']['total_question'] - student_answer_list['easy']['right']) / student_answer_list['easy']['total_question'] * 100
    if student_answer_list['medium']['total_question']!=0:
        medium_score = (student_answer_list['medium']['total_question'] - student_answer_list['medium']['right']) / student_answer_list['medium']['total_question'] * 100
    if student_answer_list['hard']['total_question']!=0:
        hard_score = (student_answer_list['hard']['total_question'] - student_answer_list['hard']['right']) / student_answer_list['hard']['total_question'] * 100
    
    suggestions = []

    # Find the appropriate suggestions based on the scores
    for course in suggestion_list["courseList"]:
        if course["Difficulty"] == "Easy" and easy_score >= int(course["Percentage"].strip('%')):
            suggestions.append({"Difficulty": "Easy", "Courses": course["Suggestion"]})
        elif course["Difficulty"] == "Medium" and medium_score >= int(course["Percentage"].strip('%')):
            suggestions.append({"Difficulty": "Medium", "Courses": course["Suggestion"]})
        elif course["Difficulty"] == "Hard" and hard_score >= int(course["Percentage"].strip('%')):
            suggestions.append({"Difficulty": "Hard", "Courses": course["Suggestion"]})

    return suggestions

def get_suggestion_list(list):
    student_answer_list = list
    # Get suggestions for the student
    suggestions = get_suggestions(student_answer_list, suggestion_list)
    
    print(suggestions)

    '''
    # Print the suggestions
    for suggestion in suggestions:
        print(f"Difficulty: {suggestion['Difficulty']}")
        for course in suggestion["Courses"]:
            print(f"CourseName: {course['CourseName']}")
            print(f"CourseLink: {course['CourseLink']}")
            print(f"CourseVideoLink: {course['CourseVideoLink']}")
        print()
        
    '''
    
    return suggestions
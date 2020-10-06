


responses = ["geometry, math", "algebra, math", "writing, english"]

# subject ($ of courses)
#   course 1
#   ..
#   course n


# english (1)
#   writing
# math (2)
#   algebra
#   geometry


from collections import defaultdict

class Solution:
  def classifySubjects(self, arr):
    # subjects = {}
    subjets = defaultdict(list)
    for item in arr:
      course_name, subject = item.split(',')
      course_name, subject = course_name.strip().lower(), subject.strip()
      subjects[subject].append(course_name)
      # if subject in subjects:
      #   subjects[subject]['count'] += 1
      #   subjects[subject]['courses'].append(course_name)
      # else:
      #   subjects[subject] = {'count': 1, 'courses': [course_name]}

    for key in sorted(subjects.keys()):
      print('{} ({})'.format(key, subjects[key]['count']))
      # print(key, '(', subjects[key]['count'], ')')
      for course_name in subjects[key]['courses']:
        print('\t ', course_name)

solution = Solution()
solution.classifySubjects(responses)

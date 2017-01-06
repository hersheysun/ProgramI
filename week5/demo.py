def subject(subject_code="CP1000", subject_name="Intro"):
    """
      :This is function that construct subject related details.
      :parm subject_code:The code associated with the subject,
      parm subject_name:The gull name of the subject(:return:string equivalent)
      :return: string equivalent
      """
    string_msg="This subject{} refer to {}".format(subject_code,subject_name)
    return string_msg
print(subject("CP1404","ProgramI"))
print(subject.__doc__)


"""
when def is evaluated, it is done only once.
the associations is preserved btw invocation.
"""
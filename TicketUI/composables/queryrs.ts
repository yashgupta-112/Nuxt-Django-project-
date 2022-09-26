export const ticketrequest = async (user: any, email: any, subject: any, priority: any, department: any, message: any) => {
    const response = await $fetch('http://127.0.0.1:8000/sysadmin', {
        method: 'POST', body: {
            'user': user,
            'email': email,
            'subject': subject,
            'priority': priority,
            'department': department,
            'message': message,


        }
    })
    // console.log(Object.values(response))

    return Object.values(response)
}


// Django model
//   user = models.CharField(max_length=255)
//   email = models.CharField(max_length=255,default='')
//   subject = models.CharField(max_length=255)
//   priority = models.CharField(max_length=255)
//   department = models.CharField(max_length=255)
//   message = models.CharField(max_length=800)
//   create_time = models.DateTimeField(auto_now_add=True)
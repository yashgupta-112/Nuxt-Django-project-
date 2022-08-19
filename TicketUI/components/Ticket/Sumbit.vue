<template>
    <div class="container">
        <h1 class="heading">Create New Support Request</h1>
        <div class="ticket-box">
            <form>
                <div class="row">
                    <div class="col-6">
                        <label for="exampleFormControlInput1" class="form-label">Username</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Username" />
                    </div>
                    <div class="col-6">
                        <label for="exampleFormControlInput1" class="form-label">Email address</label>
                        <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="Email" />
                    </div>
                </div>

                <div class="row mt-2">
                    <div class="col">
                        <label for="exampleFormControlInput1" class="form-label">Subject</label>
                        <input type="email" class="form-control" id="exampleFormControlInput1" />
                    </div>
                </div>

                <div class="row mt-3">
                    <div class="col">
                        <div class="form-floating">
                            <select class="form-select" id="floatingSelectGrid">
                                <option selected>Support</option>
                                <option value="UCP">UCP</option>
                                <option value="Sales">Sales</option>
                            </select>
                            <label for="floatingSelectGrid">Department</label>

                        </div>
                    </div>
                    <div class="col-6">
                        <div class="form-floating">
                            <select class="form-select" id="floatingSelectGrid">
                                <option selected>Medium</option>
                                <option value="Low">Low</option>
                                <option value="High">High</option>
                            </select>
                            <label for="floatingSelectGrid">Priority</label>

                        </div>
                    </div>
                </div>

                <div class="row mt-4">
                    <div class="form-floating">
                        <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea2"
                            style="height: 150px"></textarea>
                        <label for="floatingTextarea2">Add your message here...</label>
                    </div>
                </div>




                <div class="d-grid gap-2 col-2 mt-4 mx-auto">
                    <button class="btn btn-primary" type="button">Sumbit</button>

                </div>


            </form>
        </div>
    </div>
</template>

<style scoped>
@import url("../../assets/css/sysadmin.css");
</style>

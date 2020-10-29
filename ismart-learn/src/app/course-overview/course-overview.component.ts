import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-course-overview',
  templateUrl: './course-overview.component.html',
  styleUrls: ['./course-overview.component.css']
})
export class CourseOverviewComponent implements OnInit {

  constructor() { }
  buttonName = 'enable'
  disable = true

  ngOnInit(): void {
  }

  getUserFormValues(userform){
    console.log(userform)
    // console.log(userform.email)
    // console.log(userform.password)
    // console.log(userform.confirmPassword)
  }

  toggle() {
    if(this.disable){
      this.disable = false;
      this.buttonName = 'disable';
    } else{
      this.disable = true;
      this.buttonName = 'enable';
    }
  }

}

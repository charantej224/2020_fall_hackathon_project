
import { Component, OnInit } from '@angular/core';
import { CourseService } from '../course.service';

@Component({
  selector: 'app-course-overview',
  templateUrl: './course-overview.component.html',
  styleUrls: ['./course-overview.component.css']
})
export class CourseOverviewComponent implements OnInit {

  contentObj:any;
  data:string;

  constructor(private course:CourseService) {
      this.data =  "testing service";
      course.getServiceData().subscribe(response => console.log(response))
   }
   

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
    this.contentObj = this.course.getContentJson();
    this.data = this.contentObj.name;
    if(this.disable){
      this.disable = false;
      this.buttonName = 'disable';
    } else{
      this.disable = true;
      this.buttonName = 'enable';
    }
  }

}

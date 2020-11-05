import { Component, OnInit } from '@angular/core';
import { CourseService } from '../course.service';
import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-module-overview',
  templateUrl: './module-overview.component.html',
  styleUrls: ['./module-overview.component.css']
})
export class ModuleOverviewComponent implements OnInit {

  moduleObj: any[] = [];
  modulesList: any[] = [];
  contentType: string;
  constructor(private courseService: CourseService,
              private activatedRoute: ActivatedRoute) {
  }

  // tslint:disable-next-line: typedef
  ngOnInit() {
    this.activatedRoute.queryParams.subscribe(params => {
      this.contentType = params.content;
    });
    this.courseService.getContentJson().subscribe( data => {
        if (this.contentType === 'deep_learning') {
          Object.keys(data.deep_learning.modules).forEach(key => {
            this.modulesList.push(key);
            this.moduleObj.push(data.deep_learning.modules[key]);
          });
          console.log(this.moduleObj);
        } else {
          Object.keys(data.machine_learning.modules).forEach(key => {
            this.modulesList.push(key);
          this.moduleObj.push(data.machine_learning.modules[key]);
        });
        }
    });
  }

}

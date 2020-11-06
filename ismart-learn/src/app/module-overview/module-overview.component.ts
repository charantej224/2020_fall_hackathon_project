import { Component, OnInit, AfterViewInit, Renderer2, ElementRef } from '@angular/core';
import { CourseService } from '../course.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-module-overview',
  templateUrl: './module-overview.component.html',
  styleUrls: ['./module-overview.component.css']
})
export class ModuleOverviewComponent implements OnInit, AfterViewInit {

  moduleObj: any[] = [];
  modulesList: any[] = [];
  selectedModule: any;
  contentType: string;
  constructor(private courseService: CourseService,
              private renderer: Renderer2,
              private element: ElementRef,
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
          console.log(this.modulesList);
        } else {
          Object.keys(data.machine_learning.modules).forEach(key => {
            this.modulesList.push(key);
          this.moduleObj.push(data.machine_learning.modules[key]);
        });
        }
    });
  }

  ngAfterViewInit() {
    const submit = this.element.nativeElement.querySelector('#submit');
    this.renderer.listen(submit,'click',(event) => {
      console.log("heloo babe");
    });
  }
  openModule(navindex) {
    this.moduleObj.forEach((data,index) => {
      if(index === navindex) {
        this.selectedModule = data;
        console.log(navindex + this.selectedModule);
      }
    });
    
  }

}

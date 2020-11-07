import { Component, OnInit, AfterViewInit, Renderer2, ElementRef } from '@angular/core';
import { CourseService } from '../course.service';
import { ActivatedRoute } from '@angular/router';
import { mapToMapExpression } from '@angular/compiler/src/render3/util';

@Component({
  selector: 'app-module-overview',
  templateUrl: './module-overview.component.html',
  styleUrls: ['./module-overview.component.css']
})
export class ModuleOverviewComponent implements OnInit, AfterViewInit {

  moduleNames: string[] = [];
  selectedModule: any;
  contentType: string;
  moduleData: any;
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
    const contentData = this.courseService.returnContentData();
    this.moduleData = contentData[this.contentType].modules
    console.log(this.moduleData)
    Object.keys(this.moduleData).forEach((key,index) => {
      console.log(key)
      console.log(this.moduleData[key])
      this.moduleNames.push(this.moduleData[key]['name'])
  });
  }

  ngAfterViewInit() {
    const submit = this.element.nativeElement.querySelector('#submit');
    this.renderer.listen(submit, 'click', (event) => {
      console.log("heloo babe");
    });
  }
  openModule(moduleKey) {
    this.selectedModule = this.moduleData[moduleKey]
  }

}

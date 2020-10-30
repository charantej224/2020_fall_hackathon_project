import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CourseOverviewComponent } from './course-overview/course-overview.component'

const routes: Routes = [
  {
    path: "course-overview",
    component: CourseOverviewComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

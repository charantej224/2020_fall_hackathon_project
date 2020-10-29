import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'ismart-learn';
  getName(){
    return "charan"
  }
  obj = {
    name: this.getName(),
    title: this.title,
    url: window.location.href
  }
}

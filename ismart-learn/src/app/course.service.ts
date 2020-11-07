import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CourseService {

  contentJson: any;

  constructor(private httpClient: HttpClient) {
    if (!this.contentJson) {
      this.getContentJson().subscribe(data => {
        this.contentJson = data;
        console.log(this.contentJson);
      });
    }
  }

  getContentJson(): Observable<any> {
    return this.httpClient.get('assets/configuration/content.json');
  }

  getServiceData() {
    let url = 'https://jsonplaceholder.typicode.com/todos/';
    return this.httpClient.get(url);
  }

  returnContentData() {
    return this.contentJson;
  }

}

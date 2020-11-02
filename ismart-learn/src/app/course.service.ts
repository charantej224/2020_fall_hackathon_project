import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CourseService {

  constructor(private httpClient: HttpClient) { }

  getContentJson(): Observable<any> {
    return this.httpClient.get('assets/configuration/content.json');
  }

  getServiceData(){
    let url = 'https://jsonplaceholder.typicode.com/todos/';
    return this.httpClient.get(url);
  }

}

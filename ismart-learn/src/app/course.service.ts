import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class CourseService {

  constructor(private httpClient:HttpClient) { }

  getContentJson(){
    return {
      "name":"machine learning",
      "course":"introduction to machine learning"
    }
  }

  getServiceData(){
    let url = 'https://jsonplaceholder.typicode.com/todos/';
    return this.httpClient.get(url);
  }

}

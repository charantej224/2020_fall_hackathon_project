import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CourseService {

  contentJson: any;

  constructor(private httpClient: HttpClient) {
  }

  getContentJson(): Observable<any> {
    return this.httpClient.get('assets/configuration/content.json');
  }


  returnContentData() {
    return this.contentJson;
  }

  // web search links
  getWebSearch(query:string) {
    return this.httpClient.get('http://127.0.0.1:5000/api/v1/article/getwebref?query=' + query);
  }

  // video search links
  getWebvideo(query:string) {
    return this.httpClient.get('http://127.0.0.1:5000/api/v1/article/getvideoref?query=' + query);
  }

  // send abstract content 
  postAbstarct(content: string) {
    const headers = { 'content-type': 'application/json'}  
    return this.httpClient.post('http://127.0.0.1:5000/api/v1/article/summary', content, {'headers':headers}).subscribe(result => {
      console.log(result);
    });
  }

}

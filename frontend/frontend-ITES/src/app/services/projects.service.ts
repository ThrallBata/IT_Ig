import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class ProjectsService {

  constructor(private http: HttpClient) { }

  getAllProjects() {
    return this.http.get('http://127.0.0.1:8000/api/progectlist/');
  }
}

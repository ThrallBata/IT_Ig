import {Component, OnInit} from '@angular/core';
import {ProjectsService} from "../../services/projects.service";

@Component({
  selector: 'app-projects-page',
  templateUrl: './projects-page.component.html',
  styleUrls: ['./projects-page.component.scss']
})
export class ProjectsPageComponent implements OnInit {
  isProjectDetailsOpened: boolean = false;

  constructor(private projectsService: ProjectsService) {
  }

  ngOnInit(): void {
    this.projectsService.getAllProjects()
      .subscribe(res => {
        alert("Список проектов получен");
      }, error => {
        alert("Ошибка");
      });
  }
}

import { Component } from '@angular/core';
import {ProjectsPageComponent} from "../../pages/projects-page/projects-page.component";

@Component({
  selector: 'app-project-item',
  templateUrl: './project-item.component.html',
  styleUrls: ['./project-item.component.scss']
})
export class ProjectItemComponent {
  constructor(public projectsPageComponent: ProjectsPageComponent) {
  }
}

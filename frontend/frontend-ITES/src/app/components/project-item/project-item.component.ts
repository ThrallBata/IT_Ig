import {Component, Input} from '@angular/core';
import {ProjectsPageComponent} from "../../pages/projects-page/projects-page.component";
import {Project} from "../../models/project";

@Component({
  selector: 'app-project-item',
  templateUrl: './project-item.component.html',
  styleUrls: ['./project-item.component.scss']
})
export class ProjectItemComponent {
  @Input() project: Project;

  constructor(public projectsPageComponent: ProjectsPageComponent) {
  }
}

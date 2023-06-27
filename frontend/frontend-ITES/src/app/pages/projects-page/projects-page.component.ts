import {Component, OnInit} from '@angular/core';
import {ProjectsService} from "../../services/projects.service";
import {Project} from "../../models/project";
import {Chat} from "../../models/chat";

@Component({
  selector: 'app-projects-page',
  templateUrl: './projects-page.component.html',
  styleUrls: ['./projects-page.component.scss']
})
export class ProjectsPageComponent implements OnInit {
  isProjectDetailsOpened: boolean = false
  projects: Project[]

  constructor(private projectsService: ProjectsService) {
  }

  getAllProjects() {
    this.projectsService.getAllProjects()
      .subscribe((projects: Project[]) => {
        this.projects = projects;
      });
  }

  ngOnInit(): void {
    this.getAllProjects();
  }
}

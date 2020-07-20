import { Component, OnInit, ViewChild } from '@angular/core';
import { MeetupService } from '../../services/meetup.service';
import {MatAccordion} from '@angular/material/expansion';

@Component({
  selector: 'app-meetup-list',
  templateUrl: './meetup-list.component.html',
  styleUrls: ['./meetup-list.component.css']
})
export class MeetupListComponent implements OnInit {
  @ViewChild(MatAccordion) accordion: MatAccordion;
  meetups;

  constructor(
    private meetupService: MeetupService
  ) { }

  ngOnInit(): void {
    this.getAllMeetups();
  }
  
  loadData(meetup) {
    //TODO
  }

  getAllMeetups(): void {
    this.meetupService.getAll().subscribe(response => {
      this.meetups = response
    });
  }
}

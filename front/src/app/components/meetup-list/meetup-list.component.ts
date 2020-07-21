import { Component, OnInit, ViewChild } from '@angular/core';
import { MeetupService } from '../../services/meetup.service';
import { UserService } from '../../services/user.service';
import { MatAccordion } from '@angular/material/expansion';

@Component({
  selector: 'app-meetup-list',
  templateUrl: './meetup-list.component.html',
  styleUrls: ['./meetup-list.component.css']
})
export class MeetupListComponent implements OnInit {
  @ViewChild(MatAccordion) accordion: MatAccordion;
  meetups;
  isLogged: boolean = false;
  isAdmin: boolean = false;

  constructor(
    private meetupService: MeetupService,
    private userService: UserService
  ) { }

  ngOnInit(): void {
    this.isLogged = this.userService.isLogged()
    if(this.isLogged){
      this.userService.getRoles(this.userService.getUserId()).subscribe(roles => {
        Object(roles).forEach((role) => {if(role["name"] == "admin"){this.isAdmin = true;}})
      })
      this.getAllMeetups();
    }
  }
  
  loadMeetupData(meetup) {

    this.meetupService.getUsers(meetup.id).subscribe(response => {
      meetup.users = Object.keys(response).length;
    });
    this.meetupService.getTemperature(meetup.id).subscribe(response => {
      meetup.temperature = response['temperature']
    });

    if(this.isAdmin){
      this.meetupService.getBeers(meetup.id).subscribe(response => {
        meetup.beers = response['beers']
        meetup.packs = response['packs']
      });
    }
  }

  getAllMeetups(): void {
    this.meetupService.getAll().subscribe(response => {this.meetups = response});
  }
}

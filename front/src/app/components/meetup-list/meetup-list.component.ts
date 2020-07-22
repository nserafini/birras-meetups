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
  meetups: any = [];
  isLogged: boolean = false;
  isAdmin: boolean = false;
  isLoading: boolean = false;

  constructor(
    private meetupService: MeetupService,
    private userService: UserService
  ) { }

  ngOnInit(): void {
    this.isLoading = true
    this.userService.isLogged().then(logged => {
      this.isLogged = logged
      this.getAllMeetups()
      if(logged){
        this.userService.isAdmin().then(admin => {
          this.isAdmin = admin
        })
      }
    })
  }
  
  loadMeetupData(meetup) {

    this.meetupService.getTemperature(meetup.id).subscribe(response => {
      meetup.temperature = response['temperature']
    },
    (err) => {
      console.log(err)
    })

    if(this.isAdmin){
      this.meetupService.getBeers(meetup.id).subscribe(response => {
        meetup.beers = response['beers']
        meetup.packs = response['packs']
      },
      (err) => {
        console.log(err)
      })
    }
  }

  getAllMeetups(): void {
    this.meetupService.getAll().subscribe(response => {
      this.meetups = response
      this.isLoading = false
    },
    (err) => {
      console.log(err)
      this.isLoading = false
    })
  }
}

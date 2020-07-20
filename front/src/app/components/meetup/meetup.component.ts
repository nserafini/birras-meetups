import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MeetupService } from '../../services/meetup.service';

@Component({
  selector: 'app-meetup',
  templateUrl: './meetup.component.html',
  styleUrls: ['./meetup.component.css']
})
export class MeetupComponent implements OnInit {
  meetup;

  constructor(
    private route: ActivatedRoute,
    private meetupService: MeetupService
  ) { }

  ngOnInit(): void {
    this.getMeetup();
  }

  getMeetup(): void {
    let id = this.route.snapshot.paramMap.get('id');
    this.meetupService.getOne(id).subscribe(meetup => this.meetup = meetup);
  }
}

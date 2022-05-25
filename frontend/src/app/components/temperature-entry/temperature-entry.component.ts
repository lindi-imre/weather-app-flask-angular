import {Component, Input, OnInit} from '@angular/core';
import {DatePipe} from "@angular/common";

@Component({
  selector: 'app-temperature-entry',
  templateUrl: './temperature-entry.component.html',
  styleUrls: ['./temperature-entry.component.css']
})
export class TemperatureEntryComponent implements OnInit {

  @Input()
  temperature: number = 0;

  @Input()
  timestamp: number | undefined;

  constructor(pipe: DatePipe) { }

  ngOnInit(): void {
  }

  getDate(): string {
    // @ts-ignore

    const datepipe: DatePipe = new DatePipe('en-US');
    // @ts-ignore
    let formattedDate = datepipe.transform(new Date(this.timestamp * 1000), 'dd-MMM-YYYY HH:mm');

    return <string>formattedDate;
  }

  getTemperature(): number {
    return Math.floor(this.temperature - 272.15);
  }

}

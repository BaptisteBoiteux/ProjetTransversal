import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-hist-rde',
  templateUrl: './hist-rde.component.html',
  styleUrls: ['./hist-rde.component.scss']
})
export class HistRdeComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    console.log("component hist-rde créé !")
  }

  test(){
    console.log("appel fonction test du composant hist-rde")
  }
}

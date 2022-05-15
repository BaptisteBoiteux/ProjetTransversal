import { Component, OnInit } from '@angular/core';
import { Bdd2WebService } from '../bdd-2-web.service';

@Component({
  selector: 'app-connexion',
  templateUrl: './connexion.component.html',
  styleUrls: ['./connexion.component.scss']
})
export class ConnexionComponent implements OnInit {
  private userData: {id:number, login:string, passwd:string}[] = [];

  constructor(private bddService: Bdd2WebService) { }

  ngOnInit(): void {
    this.userData = this.bddService.getUsrData();
    //console.log(this.userData)
  }
}

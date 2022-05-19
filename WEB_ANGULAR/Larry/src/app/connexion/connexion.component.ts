import { Component, OnInit } from '@angular/core';
import { Bdd2WebService } from '../services/bdd-2-web.service';

@Component({
  selector: 'app-connexion',
  templateUrl: './connexion.component.html',
  styleUrls: ['./connexion.component.scss']
})
export class ConnexionComponent implements OnInit {
  constructor(private bddService: Bdd2WebService) { }

  ngOnInit(): void {
    this.bddService.getAllUsr();
    //console.log(this.userData)
  }

  onSubmit(login:string, password:string) {
    //console.log(login, password)
    this.bddService.postUsr({login,password});
  }
}

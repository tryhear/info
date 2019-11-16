package main

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
)


//UPDATE single_projec set retention_period="2",secret_level="1";
//UPDATE file set retention_period="2",secret_level="1";
//UPDATE record set retention_period="2",secret_level="1";

const(
	userName ="root"
	password ="root"
	ip       ="localhost"
	port     ="3306"
	dbName   ="wisdom-dossier"
)

func update(){
	db,err:=sql.Open("mysql",userName+":"+password+"@tcp("+ip+":"+port+")/"+dbName+"?charset=utf8")
	if err !=nil{
		fmt.Print(err)
	}
	_,err=db.Query("UPDATE single_project set retention_period='2',secret_level='1'")
	if err!=nil{
		fmt.Print(err)
	}
	_,err=db.Query("UPDATE file set retention_period='2',secret_level='1'")
	if err!=nil{
		fmt.Print(err)
	}
	_,err=db.Query("UPDATE record set retention_period='2',secret_level='1'")
	if err!=nil{
		fmt.Print(err)
	}

	fmt.Printf("\n修复完成...")
	defer db.Close()
}


func main(){
	update()
	var input string
	_, _ = fmt.Scanln(&input)
}
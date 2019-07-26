package main

import (
	_ "github.com/go-sql-driver/mysql"
	"os"
	"database/sql"
	//"github.com/jmoiron/sqlx"
	"fmt"
)


const(
	userName ="root"
	password ="root"
	ip       ="59.213.89.54"
	port     ="3306"
	dbName   ="ucamis_dy"
)

func checkErr(err error){
	if err !=nil{
		//panic("超时!")
		fmt.Print("网络超时！")
		os.Exit(9)
	}
}

func search_xm(keyword string){
	db,err:=sql.Open("mysql",userName+":"+password+"@tcp("+ip+":"+port+")/"+dbName+"?charset=utf8")
	checkErr(err)
	result,err:=db.Query("SELECT p_xmmc,p_Guid,p_Xmdh FROM `eam_project` where p_Xmmc like '%"+ keyword +"%'")

	if err!=nil{
		checkErr(err)
	}
	fmt.Printf("%-50s%-50s%-20s\n","项目名称","Guid","项目档号")
	for result.Next(){
		var(
			p_xmmc string
			p_Guid string
			p_Xmdh string
		)
		err=result.Scan(&p_xmmc,&p_Guid,&p_Xmdh)
		if err!=nil{
			checkErr(err)
		}
		fmt.Printf("%-50s%-50s%-20s\n",p_xmmc,p_Guid,p_Xmdh)
	}
	defer result.Close()
}

func search_gc(keyword string){
	db,err:=sql.Open("mysql",userName+":"+password+"@tcp("+ip+":"+port+")/"+dbName+"?charset=utf8")
	checkErr(err)
	result,err:=db.Query("select sp_Gcmc,sp_Gcdh,sp_Guid from eam_singleproject where sp_gcmc like '%"+ keyword +"%'")
	if err!=nil{
		checkErr(err)
	}
	fmt.Printf("%-50s%-20s%-50s\n","工程名称","工程档号","Guid")
	for result.Next(){
		var(
			sp_Gcmc string
			sp_Gcdh string
			sp_Guid string
		)
		err=result.Scan(&sp_Gcmc,&sp_Gcdh,&sp_Guid)
		if err!=nil{
			checkErr(err)
		}
		fmt.Printf("%-50s%-20s%-50s\n",sp_Gcmc,sp_Gcdh,sp_Guid)
	}
	defer result.Close()
}

func search_file(keyword string){
	db,err:=sql.Open("mysql",userName+":"+password+"@tcp("+ip+":"+port+")/"+dbName+"?charset=utf8")
	checkErr(err)
	result,err:=db.Query("SELECT file_ajtm,file_num FROM `eam_file` where file_ajtm like '%"+ keyword +"%'")
	if err!=nil{
		checkErr(err)
	}
	fmt.Printf("%-50s%-20s\n","案卷名称","总登记号",)
	for result.Next(){
		var(
			file_ajtm string
			file_num string
		)
		err=result.Scan(&file_ajtm,&file_num)
		if err!=nil{
			//panic(err)
			file_num="未分配"
		}
		fmt.Printf("%-50s%-20s\n",file_ajtm,file_num)
	}
	defer result.Close()
}

func search_all(keyword string){
	search_xm(keyword)
	search_gc(keyword)
	search_file(keyword)
}

func main(){
	var input string
	fmt.Print("请输入要查找的关键字：")
	_, _ = fmt.Scanln(&input)
	//fmt.Println(input)

	for{
		var searchdag string
		if input=="exit"{
			os.Exit(3)
		}else if input != ""{
			fmt.Print("请输入要查找的层级（1.项目，2.单体，3.案卷,0.返回上一级）")
			_, _ = fmt.Scanln(&searchdag)
			if searchdag=="1"{
				search_xm(input)
			}else if  searchdag=="2"{
				search_gc(input)
			}else if searchdag=="3"{
				search_file(input)
			}else if searchdag=="0" {
				input = ""
				//break
			}else if searchdag=="exit"{
				os.Exit(3)
			}else{
				search_all(input)
			}
		}else{
			fmt.Print("请输入要查找的关键字：")
			_, _ = fmt.Scanln(&input)
			//continue
		}
	}
}
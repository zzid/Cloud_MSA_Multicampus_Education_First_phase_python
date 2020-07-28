```sql
select * from emp;
#emp : 사원번호,이름,업무,관리자번호,입사일자,급여,커미션,부서번호
select * from dept;
#dept : 부서번호,부서명,도시명
select * from salgrade;
#salgrade : 등급,최저급여,최고급여

# 1. EMP TABLE 에서 이름, 급여, 커미션 금액, 총액 (SAL + COMM) 을 구하여 총액이 많은 순서로 출력하라. 
# 단 커미션이 NULL인 사람은 제외한다.

select ename, sal, comm, (sal+comm) as total
from emp
where comm is not null
order by total;

# 2. EMP와 DEPT TABLE 을 JOIN 하여 부서번호, 부서명, 이름, 급여를 출력하라.

select emp.deptno, dept.dname, emp.ename, emp.sal
from emp
inner join dept on emp.deptno = dept.deptno;


# 3. EMP 테이블에서 사원번호가 7521인 사원과 업무가 같고, 급여가 7934인 사원보다 많은 사원의
# 사원번호, 이름, 담당업무, 입사일자, 급여를 출력하여라.

select empno, ename, job,hiredate,sal
from emp
where job = (select job from emp where empno =7521)
# and sal > 7934;

# 4. EMP 테이블에서 평균급여보다 적은 급여를 받는 사원의 사원번호, 이름, 담당업무, 급여, 부서번호를 출력하라.

select empno, ename,job, sal, deptno
from emp
where sal < (select avg(sal) from emp);

# 5. EMP TABLE 에 있는 EMPNO와 MGR을 이용하여 서로의 관계를 다음과 같이 출력하라.
# SMTH의 매니저는 FORD이다.
# 5.1 (self query) 같은 emp 테이블 2개를 조인합니다.

select concat(e1.ename,'의 매니저는 ', e2.ename, '이다.')
from emp e1
inner join emp e2 on e1.mgr = e2.empno;

# 5.2 inline view
select concat(e1.ename,'의 매니저는 ', e2.ename, '이다.')
from emp e1, emp e2
where e1.mgr = e2.empno;


#6. ALLEN의 직무와 같은 사람의 이름, 부서명, 급여, 직무를 출력하라.
select *
from emp
where job = (
            select job
            from emp
            where ename = 'ALLEN')
and ename != 'ALLEN';

#7. EMP 테이블에서 SALES 부서 사원의 이름,업무를 출력하는 SELECT문을 작성하시오.
#7.1 Nested Query
select ename, job, deptno
from emp
where deptno in (select deptno
                 from dept
                 where dname = 'SALES');

#7.2 Inline View
select e.ename, e.job, e.deptno
from emp e,(select deptno from dept where dname = 'SALES') d
where e.deptno = d.deptno;


#8. EMP 테이블에서 이름에 “T”가 있는 사원이 근무하는 부서에서 근무하는 모든 사원에 대해 사원 번호,이름,급여를 출력하는 SELECT문을 작성하시오.
#단 사원번호 순으로 출력하여라.

select *
from emp
where deptno in (
    select deptno
    from emp
    where ename like '%T%'
    )
order by empno;


# 9. 전체 사원의 평균 임금보다 많은 사원의 사원번호, 이름, 부서명, 입사일, 지역, 급여를 출력하라.

select e.empno, e.ename, d.dname, e.hiredate, d.loc, e.sal
from emp e, dept d
where e.sal > (select avg(sal) from emp)
and e.deptno = d.deptno;


# 10. EMP 테이블에서 관리자중에서 부하직원을 2명이상 관리하는 관리자의 이름을 출력하세요.
# 10.1 Nested Query (where 절에 subquery)

select ename
from emp
where (select e.mgr from (select mgr, count(*) as cnt from emp group by mgr) e where e.cnt >= 2)  = empno;



# 10.2 Inline View (from 절에 subquery)

select ename
from emp e, (select mgr, count(*) as cnt from emp group by mgr having cnt >= 2) m
where e.empno = m.mgr;


# 11.EMP 테이블에서 CHICAGO에서 근무하는 사원과 같은 업무를 하는 사원의 이름,업무를 출력하는 SELECT문을 작성하시오.

select ename, job
from emp
where job in (select job from emp where deptno = (select deptno from dept where loc = 'CHICAGO'));


# 12.EMP 테이블에서 업무가 JONES와 같거나 월급이 FORD이상인 사원의 이름,업무,부서번호,급여를 출력하는 SELECT문을 작성하시오.
# 단 업무별, 월급이 많은 순으로 출력하여라.

select ename, job, deptno, sal
from emp
group by job asc , sal desc
having (job = (select job from emp where ename = 'JONES')) || (sal >= (select sal from emp where ename ='FORD'));

select ename, job, deptno, sal
from emp
where job = (select job from emp where ename = 'JONES') || sal >= (select sal from emp where ename ='FORD');

select * from dept


# 13. EMP 테이블에서 업무별로 최소 급여를 받는 사원의 사원번호, 이름, 업무, 입사일자, 급여, 부서번호를 출력하여라.

select empno, ename, job, hiredate, sal, deptno
from emp
where sal in (select min(sal) from emp group by job);


# 14. emp와 dept 테이블에서 업무가 manager인 사원의 이름, 업무, 부서명, 근무지를 출력하여라.
# Inline View 를 사용하자

select e.ename, e.job, e.deptno, d.loc
from dept d, (select * from emp where job = 'MANAGER') e
where d.deptno = e.deptno;


# 15. EMP 테이블에서 30번 부서원 중 최저급여를 받는 사원을 제외한 나머지 사원들의 모든 정보를 출력하는 SELECT문을 작성하시오.
select *
from emp
where deptno = 30 and sal != (select min(sal) from emp where deptno = 30);



# 16. EMP 테이블에서 말단 사원의 사원번호,이름,업무,부서번호를 출력하는 SELECT문을 작성하시오.(말단사원: 다른 사원을 관리하지 않는 사원)
# - ORACLE : NVL(VALUE1, VALUE2)
# - MSSQL  : ISNULL(VALUE1, VALUE2)
# - MYSQL  : IFNULL(VALUE1, VALUE2)
SELECT DISTINCT(IFNULL(mgr,0)) FROM emp;

select *
from emp
where empno not in (select e1.empno from emp e1, emp e2 where e1.empno = e2.mgr)


# 17. EMP 테이블에서 사원번호, 이름, 업무, 급여, 급여의 등급을 출력하되 3등급 이상인 사원의 정보만을 출력하세요.
# (emp와 salgrade 테이블을 이용);
select *
from emp
where emp.sal >=
      (   select min(LOSAL)
          from salgrade
          where GRADE >= 3
      );


# 18. 부서번호, 부서에 속한 직원수, 부서명, 도시명을 출력하세요.
# 직원수가 5명이상인 부서만 출력하세요. ( inline view )

select e.deptno, cnt, e.dname, e.loc
from (select emp.deptno, count(empno) as cnt, dept.dname,dept.loc
      from emp
      inner join dept on dept.deptno = emp.deptno
      group by emp.deptno) e
where e.cnt >= 5;


# 20. EMP 테이블에서 적어도 한 명 이상으로부터 보고를 받을 수 있는 사원의 업무,이름,사원번호,부서번호를 출력하시오.
# (즉 다른 사원을 관리자를 출력하세요)
select e1.job, e1.ename,e1.empno, e1.deptno
from emp e1
inner join emp e2 on e1.empno = e2.mgr
```
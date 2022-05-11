DROP TABLE IF EXISTS companies;
CREATE TABLE companies (
  fiscalYear real,
  company text,
  initialApprovals real,
  initialDenials real,
  continuingApprovals real,
  continuingDenials real,
  companyState text,
  companyCity text,
  companyZIP real
);
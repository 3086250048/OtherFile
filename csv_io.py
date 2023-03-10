from csv import reader,writer
from collections import namedtuple
from os import getcwd,chdir
class CsvIo():
  
    def __init__(
        self,
        filename:str | None=None,
        delimiter:str | None=',',
        encoding:str| None='utf-8',
        readrowcolumn:iter=(),
        writecontent:iter =(),
        csvmode:str | None =None,
        filemode:str | None = None,
        linebreak:str | None = '\n'
        ) -> None:
  
        self._filename=filename
        self._delimiter=delimiter
        self._encoding=encoding
        self._readrowcloumn=readrowcolumn
        self._writecontent=writecontent
        self._csvmode=csvmode
        self._filemode=filemode
        self._linebreak=linebreak
  
    @property
    def filename(self):
        return self._filename
    @filename.setter
    def filename(self,filename:str|None = None):
        self._filename= filename
    @property
    def delimiter(self):
        return self._delimiter
    @delimiter.setter
    def delimiter(self,delimiter:str|None = None):
        self._delimiter= delimiter
    @property
    def encoding(self):
        return self._encoding
    @encoding.setter
    def encoding(self,encoding:str|None=None):
        self._encoding=encoding
    @property
    def readrowcolumn(self):
        return self._readrowcloumn
    @readrowcolumn.setter
    def readrowcolumn(self,readrowcolumn:iter=()):
        self._readrowcloumn=readrowcolumn
    @property
    def writecontent(self):
        return self._writecontent
    @writecontent.setter
    def writecontent(self,writecontent:iter=()):
        self._writecontent=writecontent
    @property
    def csvmode(self):
        return self._csvmode
    @csvmode.setter
    def csvmode (self,csvmode:str|None=None):
        self._csvmode=csvmode
    @property
    def filemode(self):
        return self._filemode
    @filemode.setter
    def filemode (self,filemode:str|None=None):
        self._filemode=filemode
    @property
    def linebreak(self):
        return self._linebreak
    @linebreak.setter
    def linebreak (self,linebreak:str|None=None):
        self._linebreak=linebreak

    def get_csv(self) -> tuple:
        with open(self.filename,self.filemode,encoding=self.encoding) as file_obj:
            csv_obj =reader(file_obj,delimiter=self.delimiter)
            return tuple(csv_obj)
    
    def read_csv(self) -> list | str :
        if len(self.readrowcolumn) == 0 : 
            return self.get_csv()
        if len(self.readrowcolumn) == 1 : return self.get_csv()[self.readrowcolumn[0]]
        if len(self.readrowcolumn) == 2 : return self.get_csv()[self.readrowcolumn[0]][self.readrowcolumn[1]]


    def write_csv(self) -> None:
        with open(self.filename,self.filemode,encoding=self.encoding) as file_obj:
            csv_obj= writer(file_obj,delimiter=self.delimiter,lineterminator=self.linebreak)
            print(1)
            if self.csvmode == 'single' :csv_obj.writerow([self.writecontent]) 
            if self.csvmode == 'multi' :csv_obj.writerows(self.writecontent)

    def __str__(self):
        return f'root_path:{getcwd()}'
    

if __name__ == '__main__':
     obj=CsvIo()

    # chdir(getcwd()+'/Core/dev_file')
    # obj.filename='dad.csv'
    # obj.filemode='w'
    # obj.csvmode='multi'
    # obj.writecontent=(['asdadada'],['sadasdadasd'],['asdasdadad'])
    # obj.write_csv()
    # print(obj)
 



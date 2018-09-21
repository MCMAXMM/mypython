import argparse
import sys
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--x",type=float,default=1.0,help="what is the first number?")
    parser.add_argument("--y",type=float,default=1.0,help="what is the second number")
    parser.add_argument("--operation",type=str,default=1.0,help="what operation?(add,sub,mul,or div)")
    args=parser.parse_args(
        sys.stdout.write(str(calc(args)))
    )
def calc(args):
    if args.operation=="add":
        return args.x+args.y
    elif args.operation=="sub":
        return args.x-args.y
    elif args.operation=="mul":
        return args.x*args.y
    elif args.operation=="div":
        return args.x/args.y
if __name__ == '__main__':
    main()
#在命令行输入 python file_path --x=5 --y=3 --operation="add"  
#也可以输入 -h查询帮助文档
#上面的main函数可以改成
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--x",type=float,default=1.0,help="what is the first number?")
    parser.add_argument("--y",type=float,default=1.0,help="what is the second number")
    parser.add_argument("--operation",type=str,default=1.0,help="what operation?(add,sub,mul,or div)")
    # args=parser.parse_args(
    #     sys.stdout.write(str(calc(args)))#不适用sys.stdout
    args=parser.parse_args()#正常解析函数
    print(calc(args))#把args传递过去，通过args.variable来使用参数

using System.Collections;using System.Reflection;using System.Runtime.Loader;using System.Text;
Console.OutputEncoding=Encoding.UTF8;
var root=@"D:\newMir3"; var deps=Path.Combine(root,"tools","_deps");
AssemblyLoadContext.Default.Resolving+=(_,a)=>{foreach(var d in new[]{deps,root}){var p=Path.Combine(d,(a.Name??"")+".dll");if(File.Exists(p))return AssemblyLoadContext.Default.LoadFromAssemblyPath(p);}return null;};
var lib=AssemblyLoadContext.Default.LoadFromAssemblyPath(Path.Combine(root,"Library.dll"));
var st=lib.GetType("MirDB.Session")!; var sm=lib.GetType("MirDB.SessionMode")!; var mode=Enum.Parse(sm,"ServerTool");
var ctor=st.GetConstructor(new[]{sm,typeof(Assembly[]),typeof(bool),typeof(string),typeof(string),typeof(string)})!;
var get=st.GetMethods().Single(m=>m.Name=="GetCollection"&&m.IsGenericMethodDefinition&&m.GetParameters().Length==0);
string Slash(string x)=>Path.EndsInDirectorySeparator(x)?x:x+Path.DirectorySeparatorChar;
string S(object? o,string n)=>o==null?"":Convert.ToString(o.GetType().GetProperty(n)?.GetValue(o))??"";
int Iv(object? o,string n){var v=o?.GetType().GetProperty(n)?.GetValue(o);return v==null?0:Convert.ToInt32(v);}
object? P(object? o,string n)=>o?.GetType().GetProperty(n)?.GetValue(o);
var work=Path.Combine(Path.GetTempPath(),"mir3-b143-"+Guid.NewGuid().ToString("N")[..8]); var bak=work+"_b";
Directory.CreateDirectory(work);Directory.CreateDirectory(bak);
File.Copy(Path.Combine(root,"Database","System.db"),Path.Combine(work,"System.db"),true);
File.Copy(Path.Combine(root,"Database","ClientSystem.db"),Path.Combine(work,"ClientSystem.db"),true);
var ses=ctor.Invoke(new object[]{mode,new[]{lib},false,"",Slash(work),Slash(bak)});
st.GetMethod("Init",Type.EmptyTypes)!.Invoke(ses,null);
var buffT=lib.GetType("Library.SystemModels.CustomBuffInfo")!;
var statT=lib.GetType("Library.SystemModels.CustomBuffInfoStat")!;
var buffs=((IEnumerable)get.MakeGenericMethod(buffT).Invoke(ses,null)!).Cast<object>().ToList();
var stats=((IEnumerable)get.MakeGenericMethod(statT).Invoke(ses,null)!).Cast<object>().ToList();
Console.WriteLine("CustomBuffInfoStat props="+string.Join(",",statT.GetProperties().Select(p=>p.Name)));
var b=buffs.First(x=>Iv(x,"Index")==143);
var bs=P(b,"BuffStats");
Console.WriteLine("BuffStats type="+bs?.GetType().FullName);
if (bs is System.Collections.IEnumerable en) foreach(var s in en) Console.WriteLine($"  stat={S(s,"Stat")} val={P(s,"Amount")??P(s,"Value")}");
foreach(var s in stats.Where(x=>Iv(P(x,"Buff")??P(x,"CustomBuff")??x,"Index")==143 || object.ReferenceEquals(P(x,"Buff"),b) || object.ReferenceEquals(P(x,"CustomBuff"),b) || S(P(x,"Buff"),"BuffName").Contains("\u6302\u673a")))
  Console.WriteLine($"STAT link idx={Iv(s,"Index")} buff={S(P(s,"Buff")??P(s,"CustomBuff"),"BuffName")}#{Iv(P(s,"Buff")??P(s,"CustomBuff"),"Index")} Stat={S(s,"Stat")} Amount={P(s,"Amount")}");
// also search DropRate on any custom buff
foreach(var s in stats) {
  if (S(s,"Stat").Contains("Drop")) {
    var bb=P(s,"Buff")??P(s,"CustomBuff");
    Console.WriteLine($"DROPRATE buff={S(bb,"BuffName")}#{Iv(bb,"Index")} Stat={S(s,"Stat")} Amount={P(s,"Amount")}");
  }
}
(ses as IDisposable)?.Dispose();

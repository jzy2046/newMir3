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
bool Bv(object? o,string n){var v=o?.GetType().GetProperty(n)?.GetValue(o);return v!=null&&Convert.ToBoolean(v);}
object? P(object? o,string n)=>o?.GetType().GetProperty(n)?.GetValue(o);
void Check(string label, string dbFile){
  var work=Path.Combine(Path.GetTempPath(),"mir3-vcli-"+Guid.NewGuid().ToString("N")[..8]); var bak=work+"_b";
  Directory.CreateDirectory(work);Directory.CreateDirectory(bak);
  File.Copy(dbFile, Path.Combine(work,"System.db"), true);
  var ses=ctor.Invoke(new object[]{mode,new[]{lib},false,"",Slash(work),Slash(bak)});
  st.GetMethod("Init",Type.EmptyTypes)!.Invoke(ses,null);
  var npcs=((IEnumerable)get.MakeGenericMethod(lib.GetType("Library.SystemModels.NPCInfo")!).Invoke(ses,null)!).Cast<object>().ToList();
  var maps=((IEnumerable)get.MakeGenericMethod(lib.GetType("Library.SystemModels.MapInfo")!).Invoke(ses,null)!).Cast<object>().ToList();
  var buffs=((IEnumerable)get.MakeGenericMethod(lib.GetType("Library.SystemModels.CustomBuffInfo")!).Invoke(ses,null)!).Cast<object>().ToList();
  string wst="\u4e07\u4e8b\u901a"; string weg="\u6c83\u5c14\u9601"; string xbsm="\u897f\u90e8\u6c99\u6f20"; string gj="\u6302\u673a";
  var wstN=npcs.Where(x=>S(x,"NPCName").Contains(wst)).ToList();
  Console.WriteLine(label+" wst="+wstN.Count+" hidden="+wstN.Count(x=>Bv(x,"Display"))+" visible="+wstN.Count(x=>!Bv(x,"Display")));
  foreach(var n in wstN) Console.WriteLine($"  {Iv(n,"Index")} {S(n,"NPCName")} Display={Bv(n,"Display")}");
  Console.WriteLine(label+" weg="+npcs.Count(x=>S(x,"NPCName").Contains(weg)));
  Console.WriteLine(label+" westmap="+maps.Count(x=>S(x,"Description")==xbsm));
  Console.WriteLine(label+" gjbuff="+buffs.Count(x=>S(x,"BuffName").Contains(gj)));
  (ses as IDisposable)?.Dispose(); try{Directory.Delete(work,true);}catch{} try{Directory.Delete(bak,true);}catch{}
}
Check("SYS", Path.Combine(root,"Database","System.db"));
Check("CLI", Path.Combine(root,"Database","ClientSystem.db"));
Check("DATACLI", Path.Combine(root,"Data","ClientSystem.db"));

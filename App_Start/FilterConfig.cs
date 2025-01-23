using System.Web;
using System.Web.Mvc;

namespace Funktsioonide_print___input____float____int___kasutamine
{
    public class FilterConfig
    {
        public static void RegisterGlobalFilters(GlobalFilterCollection filters)
        {
            filters.Add(new HandleErrorAttribute());
        }
    }
}

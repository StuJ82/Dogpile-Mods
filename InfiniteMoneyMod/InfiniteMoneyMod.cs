using BepInEx;
using BepInEx.Logging;
using HarmonyLib;
using System.Reflection;
using JetBrains.Annotations;
using Obvious.Soap;
namespace InfiniteMoneyMod
{
    [BepInPlugin(PluginInfo.PLUGIN_GUID, PluginInfo.PLUGIN_NAME, PluginInfo.PLUGIN_VERSION)]
    public class Plugin : BaseUnityPlugin
    {
        [CanBeNull] public static Plugin Instance;
        // Public accessor so other classes can log via the BepInEx logger safely
        [CanBeNull] public static ManualLogSource Log => Instance?.Logger;

        [CanBeNull] public static IntVariable moneyAsset;
        private const int DesiredMoney = 999999;

        private void Awake()
        {
            Instance = this;
            Harmony.CreateAndPatchAll(Assembly.GetExecutingAssembly(), PluginInfo.PLUGIN_GUID);
        }

        private void Update()
        {
            try
            {
                if (moneyAsset != null)
                {
                    moneyAsset.Value = DesiredMoney;
                }
            }
            catch (System.Exception e)
            {
                // Use the instance logger (protected in BaseUnityPlugin) to report errors
                Logger.LogError($"Update error: {e}");
                // do not rethrow to avoid crashing the game
            }
        }
    }

    [HarmonyPatch(typeof(PlayerMoney), "Start")]
    public static class StartingMoney
    {
        static void Postfix(PlayerMoney __instance)
        {
                FieldInfo field = AccessTools.Field(typeof(PlayerMoney), "_playerMoneyAsset");
                var val = field.GetValue(__instance);
                Plugin.moneyAsset = val as IntVariable;
                
                Plugin.Log?.LogInfo($"_playerMoneyAsset value: {val?.GetType().FullName ?? "null"}");
                Plugin.Log?.LogInfo($"Money assigned. IntVariable cast success: {Plugin.moneyAsset != null}");
        }
    }

    public class PluginInfo
    {
        public const string PLUGIN_NAME = "Infinite Money Mod";
        public const string PLUGIN_VERSION = "1.0.0";
        public const string PLUGIN_GUID = "InfiniteMoneyModDogpile";
    }
}
 
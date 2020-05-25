using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


static class myExtensions
{
    private static System.Random rng = new System.Random();

    public static void Shuffle<T>(this IList<T> list)
    {
        int n = list.Count;
        while (n > 1)
        {
            n--;
            int k = rng.Next(n + 1);
            T value = list[k];
            list[k] = list[n];
            list[n] = value;
        }
    }
}

public class Carta
{
    public Carta(int n, char p, int v, int pr)
    {
        num = n;
        pal = p;
        valor = v;
        prioritat = pr;
    }

    public Carta(Carta c)
    {
        num = c.num;
        pal = c.pal;
        valor = c.valor;
        prioritat = c.prioritat;
    }

    public int num;
    public char pal;
    public int valor;
    public int prioritat;
    static float W_pinta = 10;
    
    public float cost(Carta pinta)
    {
        float c = prioritat;
        if(pal == pinta.pal)
        {
            c *= W_pinta;
        }
        return c;
    }

    public string bonica()
    {
        string nom = num.ToString();
        switch (pal)
        {
            case 'c':
                nom += " de copes";
                break;
            case 'e':
                nom += " d'espases";
                break;
            case 'b':
                nom += " de bastos";
                break;
            case 'o':
                nom += " d'oros";
                break;
        }
        return nom;
    }

    public string bonicaBotons()
    {
        string nom = num.ToString();
        switch (pal)
        {
            //ìJUGAR!12!D’ESPASESí
            case 'c':
                nom += "!DE!COPESí";
                break;
            case 'e':
                nom += "!D’ESPASESí";
                break;
            case 'b':
                nom += "!DE!BASTOSí";
                break;
            case 'o':
                nom += "!D’OROSí";
                break;
        }
        return nom;
    }
}

public class mainLoop : MonoBehaviour
{
    public Button ButtStart, ButtC1, ButtC2, ButtC3;
    public Animation anim;
    public GameObject CartaMa1;
    public GameObject CartaMa2;
    public GameObject CartaMa3;
    public GameObject CartaJEntry;
    public GameObject CartaJ;
    public GameObject CartaJAux;
    public GameObject Pila;
    public GameObject CartaPinta;
    public Text TextMaIA;
    public Text TextMaH;
    public Text TextPinta;
    public Text TextCartesTaula;
    public Text TextPuntsIA;
    public Text TextPuntsH;
    public Text TextPila;
    public Text TextFinal;
    public Text TextGeneral;
    public Button sortirDelJoc;

    public Text TextInfo;
    public Text TextCartesTaula2;
    public Text TextPila2;
    public Text TextPinta2;
    public Text TextPuntsFinal;
    public GameObject panell;


    public AudioSource s;
    public AudioClip soVictoriaH;
    public AudioClip soVictoriaIA;
    public AudioClip[] sonsIAGuanyaRonda;
    public AudioClip[] sonsIAPerdRonda;
    public AudioClip somhi;
    //private (int, char)[] baralla = { new (int,char){ 1, 'b' }, { 2, 'b' }, { 3, 'b' }, { 4, 'b' }, { 5, 'b' }, { 6, 'b' }, { 7, 'b' }, { 8, 'b' }, { 9, 'b' }, { 10, 'b' }, { 11, 'b' }, { 12, 'b' }, { 1, 'e' }, { 2, 'e' }, { 3, 'e' }, { 4, 'e' }, { 5, 'e' }, { 6, 'e' }, { 7, 'e' }, { 8, 'e' }, { 9, 'e' }, { 10, 'e' }, { 11, 'e' }, { 12, 'e' }, { 1, 'o' }, { 2, 'o' }, { 3, 'o' }, { 4, 'o' }, { 5, 'o' }, { 6, 'o' }, { 7, 'o' }, { 8, 'o' }, { 9, 'o' }, { 10, 'o' }, { 11, 'o' }, { 12, 'o' }, { 1, 'c' }, { 2, 'c' }, { 3, 'c' }, { 4, 'c' }, { 5, 'c' }, { 6, 'c' }, { 7, 'c' }, { 8, 'c' }, { 9, 'c' }, { 10, 'c' }, { 11, 'c' }, { 12, 'c' } };

    private List<Carta> baralla = new List<Carta>();


    // private List<Carta> maIA = new List<Carta>();
    // private List<Carta> maHuma = new List<Carta>();
    private Carta[] maIA = new Carta[3];
    private Carta[] maHuma = new Carta[3];

    private Carta pinta;
    private int puntsH = 0;
    private int puntsIA = 0;

    //private Dictionary<int, int> valorNumeros = new Dictionary<int, int>() { { 1, 11 }, { 3, 10 }, { 12, 4 }, { 11, 3 }, { 10, 2 }, { 9, 0 }, { 8, 0 }, { 7, 0 }, { 6, 0 }, { 5, 0 }, { 4, 0 }, { 2, 0 } };
    //private Dictionary<int, int> prioritat_base = new Dictionary<int, int>() { { 1, 12 }, { 3, 11 }, { 12, 10 }, { 11, 9 }, { 10, 8 }, { 9, 7 }, { 8, 6 }, { 7, 5 }, { 6, 4 }, { 5, 3 }, { 4, 2 }, { 2, 1 } };

    //private List<Carta> cartesSobreLaTaula = new List<Carta>();
    private Carta[] cartesSobreLaTaula = new Carta[2]; //IMPORTANT: POS 0 -> IA; POS 1 -> H      SEMPRE!

    //private Stack<Carta> cartesGuanyadesIA = new Stack<Carta>();
    //private Stack<Carta> cartesGuanyadesH = new Stack<Carta>();

    private bool comencaH;
    private bool pause = true;

    int valorNumeros(int num)
    {
        if (num != null)
        {
            switch (num)
            {
                case 1: return 11; break;
                case 3: return 10; break;
                case 12: return 4; break;
                case 11: return 3; break;
                case 10: return 2; break;
                default: return 0; break;
            }
        }
        else
        {
            return -1;
        }

    }

    int prioritat_base(int num)
    {
        if (num != null)
        {
            switch (num)
            {
                case 1: return 12; break;
                case 3: return 11; break;
                case 12: return 10; break;
                case 11: return 9; break;
                case 10: return 8; break;
                case 9: return 7; break;
                case 8: return 6; break;
                case 7: return 5; break;
                case 6: return 4; break;
                case 5: return 3; break;
                case 4: return 2; break;
                case 2: return 1; break;
                default: return 0; break;
            }
        }
        else
        {
            return -1;
        }

    }

    private string estat;


    bool guanyaIA(Carta cartaIA, Carta cartaH) //, bool comencaH, Carta pinta)
    {
        if (cartaIA.pal == pinta.pal && cartaH.pal != pinta.pal)
        {
                return true;
        } else if (cartaIA.pal != pinta.pal && cartaH.pal == pinta.pal)
            {
                return false;
            } else {
                if (comencaH && cartaIA.pal != cartaH.pal)                
                {
                    return false;
                } else if (!comencaH && cartaIA.pal != cartaH.pal)
                {
                    return true;
                }
                else
                {
                    if(cartaIA.prioritat > cartaH.prioritat)
                    {
                        return true;
                    }
                    else
                    {
                        return false;
                    }
                }
            }
    }

    float benefici(Carta cartaH, Carta cartaIA)
    {
        float b = cartaH.valor + cartaIA.valor;
        if (!guanyaIA(cartaIA, cartaH))
        {
            b = -b;
        }
        return b;
    }

    static float W_benefici = 9.5f;
    static float W_cost = 2;

    float h(Carta cartaIA, Carta cartaH)
    {
        float h = 0;
        if (!comencaH)
        {
            h = -cartaIA.cost(pinta);
        }
        else
        {
            h = benefici(cartaH, cartaIA) * W_benefici - cartaIA.cost(pinta) * W_cost;
        }
        return h;
    }

    int triarCarta(Carta cartaH)
    {
        int indexSelec = 0;
        //float h_CartaSelec = h(maIA[0], cartaH);
        float h_CartaSelec = -500; //lleig pero es lo que hay
        for (int i = 0; i <maIA.Length; i++)
        {
            if (maIA[i] != null)
            {
                float h_aux = h(maIA[i], cartaH);
                if (h_aux > h_CartaSelec)
                {
                    h_CartaSelec = h_aux;
                    indexSelec = i;
                }
            }
        }
        return indexSelec;
    }

    bool animacio1Feta;
    bool animacio2Feta;
    bool animacio3Feta;
    bool animacio4Feta;
    bool animacio5Feta;
    bool animacio6Feta;

    static System.Random rnd = new System.Random();

    void Start()
    {
        anim = GetComponent<Animation>();


        ButtStart.onClick.AddListener(OnClickStartPause);
        
        ButtC1.onClick.AddListener(() => OnClickCarta(0));
        ButtC2.onClick.AddListener(() => OnClickCarta(1));
        ButtC3.onClick.AddListener(() => OnClickCarta(2));

        sortirDelJoc.onClick.AddListener(Application.Quit);

        char[] pals = { 'b', 'c', 'e', 'o' };

        for (int i = 1; i < 13; i++) /////////////////////////////////////////////////////////////////////OJUT - 13
        {
            foreach (char pal in pals)
            {
                int v = valorNumeros(i);
                int prio = prioritat_base(i);
                Carta c = new Carta(i, pal, v, prio);
                baralla.Add(c);
            }
        }
        myExtensions.Shuffle<Carta>(baralla);

        estat = "IniciPartida";


        //estat = "QuiGuanyaJoc";


        animacio1Feta = false;
        animacio2Feta = false;
        animacio3Feta = false;
        animacio4Feta = false;
        animacio5Feta = false;
        animacio6Feta = false;
        comencaH = false;

    }

    int cartaTriada;
    int CartaTriadaH = -1;
    bool nomesQuedaPinta = false;
    string instr = "";
    void Update()
    {

        if (!pause)
        {
            switch (estat)
            {
                case "IniciPartida":
                    //animacio posarpinta

                    if (!animacio1Feta)
                    {
                        //Provisionalment va aqui, perque aixi nomes es faci un cop. Realment va a l'if animaciofeta de la de posarpinta
                        pinta = baralla[0];
                        baralla.RemoveAt(0);

                        CartaMa1.SetActive(true);
                        anim.Play("getC1");
                        animacio1Feta = true;
                        s.PlayOneShot(somhi,1F);
                    }
                    if (!anim.IsPlaying("getC1") && animacio1Feta)
                    {
                        if (!animacio2Feta)
                        {
                            CartaMa2.SetActive(true);
                            anim.Play("getC2");
                            animacio2Feta = true;
                        }
                        if (!anim.IsPlaying("getC2") && animacio2Feta)
                        {
                            if (!animacio3Feta)
                            {
                                CartaMa3.SetActive(true);
                                anim.Play("getC3");
                                animacio3Feta = true;
                            }

                            if (!anim.IsPlaying("getC3") && animacio3Feta)
                            {

                                if (!animacio4Feta)
                                {
                                    //Aqui dins per estalviar-me de crear un altre boolea

                                    //maIA.Add(baralla[0]);
                                    maIA[0] = baralla[0];
                                    baralla.RemoveAt(0);
                                    //maIA.Add(baralla[0]);
                                    maIA[1] = baralla[0];
                                    baralla.RemoveAt(0);
                                    //maIA.Add(baralla[0]);
                                    maIA[2] = baralla[0];
                                    baralla.RemoveAt(0);

                                    CartaJEntry.SetActive(true);
                                    anim.Play("Hget");
                                    animacio4Feta = true;
                                }
                                if (!anim.IsPlaying("Hget") && animacio4Feta)
                                {
                                    if (!animacio5Feta)
                                    {
                                        anim.Play("Hget");
                                        animacio5Feta = true;
                                        maHuma[0] = baralla[0];
                                        baralla.RemoveAt(0);
                                    }
                                    if (!anim.IsPlaying("Hget") && animacio5Feta)
                                    {
                                        if (!animacio6Feta)
                                        {
                                            anim.Play("Hget");
                                            animacio6Feta = true;
                                            maHuma[1] = baralla[0];
                                            baralla.RemoveAt(0);
                                        }
                                        if (!anim.IsPlaying("Hget") && animacio6Feta)
                                        {
                                            estat = "IATria";
                                            //maHuma.Add(baralla[0]);

                                            //maHuma.Add(baralla[0]);

                                            //maHuma.Add(baralla[0]);
                                            maHuma[2] = baralla[0];
                                            baralla.RemoveAt(0);

                                            CartaJEntry.SetActive(false);

                                            animacio1Feta = false;
                                            animacio2Feta = false;
                                            animacio3Feta = false;
                                            animacio4Feta = false;
                                            animacio5Feta = false;
                                            animacio6Feta = false;
                                        }
                                    }
                                }
                            }
                        }
                    }
                    break;
                case "IATria":
                    if (comencaH)
                    {
                        cartaTriada = triarCarta(cartesSobreLaTaula[1]);
                    }
                    else
                    {
                        cartaTriada = triarCarta(null);
                    }
                    estat = "IAJuga";
                    break;
                case "IAJuga":
                    instr = "throwC" + (cartaTriada + 1).ToString();
                    if (!animacio1Feta)
                    {
                        anim.Play(instr);
                        animacio1Feta = true;
                    }
                    if (!anim.IsPlaying(instr) && animacio1Feta)
                    {
                        cartesSobreLaTaula[0] = maIA[cartaTriada];
                        maIA[cartaTriada] = null;

                        if (comencaH)
                        {
                            estat = "QuiGuanyaRonda";
                        }
                        else
                        {
                            estat = "EsperantH";
                        }
                        animacio1Feta = false;
                    }
                    break;
                case "EsperantH":
                    /*if (maHuma[0] != null) ButtC1.gameObject.SetActive(true);
                    if (maHuma[1] != null) ButtC2.gameObject.SetActive(true);
                    if (maHuma[2] != null) ButtC3.gameObject.SetActive(true);*/

                    if (ButtC1.gameObject.active) ButtC1.interactable = true;
                    if (ButtC2.gameObject.active) ButtC2.interactable = true;
                    if (ButtC3.gameObject.active) ButtC3.interactable = true;

                    if (CartaTriadaH != -1)
                    {
                        /*ButtC1.gameObject.SetActive(false);
                        ButtC2.gameObject.SetActive(false);
                        ButtC3.gameObject.SetActive(false);*/
                        ButtC1.interactable = false;
                        ButtC2.interactable = false;
                        ButtC3.interactable = false;
                        estat = "HJuga";
                    }
                    break;
                case "HJuga":
                    if (!animacio1Feta)
                    {
                        CartaJEntry.SetActive(true);
                        anim.Play("Hthrow");
                        animacio1Feta = true;
                    }
                    if (!anim.IsPlaying("Hthrow") && animacio1Feta)
                    {
                        cartesSobreLaTaula[1] = maHuma[CartaTriadaH];
                        maHuma[CartaTriadaH] = null;

                        if (comencaH)
                        {
                            estat = "IATria";
                        }
                        else
                        {
                            estat = "QuiGuanyaRonda";
                        }
                        animacio1Feta = false;
                        CartaJEntry.SetActive(false);
                        CartaJ.SetActive(true);
                    }
                    break;
                case "QuiGuanyaRonda": //per no fer un altre boolea, canvio aqui ja el valor de comencaH, per saber en estats posteriors qui ha guanyat
                    if (guanyaIA(cartesSobreLaTaula[0], cartesSobreLaTaula[1]))
                    {
                        comencaH = false; //Ha guanyat la IA pel que a la següent ronda començarà aquesta
                        int r = rnd.Next(sonsIAGuanyaRonda.Length);
                        s.PlayOneShot(sonsIAGuanyaRonda[r],1F);
                        estat = "IARecull";
                    }
                    else
                    {
                        comencaH = true;  //Ha guanyat l'humà pel que a la següent ronda començarà aquest
                        int r = rnd.Next(sonsIAPerdRonda.Length);
                        s.PlayOneShot(sonsIAPerdRonda[r],1F);
                        estat = "HRecull";
                    }
                    break;
                case "IARecull":
                    if (!animacio1Feta)
                    {
                        switch (cartaTriada)
                        {
                            case 0: CartaMa1.SetActive(false); break;
                            case 1: CartaMa2.SetActive(false); break;
                            case 2: CartaMa3.SetActive(false); break;
                        }
                        anim.Play("recullCartes");
                        animacio1Feta = true;
                    }
                    if (!anim.IsPlaying("recullCartes") && animacio1Feta)
                    {
                        puntsIA += cartesSobreLaTaula[0].valor + cartesSobreLaTaula[1].valor;

                        cartesSobreLaTaula[0] = null;
                        cartesSobreLaTaula[1] = null;
                        if (maIA[0] == null && maIA[1] == null && maIA[2] == null) //no té cartes a la ma = final de partida
                        {
                            estat = "QuiGuanyaJoc";
                        }
                        else estat = "IARoba";

                        animacio1Feta = false;
                        CartaJ.SetActive(false);
                    }
                    break;
                case "HRecull":
                    if (!animacio1Feta)
                    {
                        switch (cartaTriada)
                        {
                            case 0: CartaMa1.SetActive(false); break;
                            case 1: CartaMa2.SetActive(false); break;
                            case 2: CartaMa3.SetActive(false); break;
                        }
                        CartaJAux.SetActive(true);
                        CartaJ.SetActive(false);
                        anim.Play("HRecullCartes");
                        animacio1Feta = true;
                    }
                    if (!anim.IsPlaying("HRecullCartes") && animacio1Feta)
                    {
                        puntsH += cartesSobreLaTaula[0].valor + cartesSobreLaTaula[1].valor;

                        cartesSobreLaTaula[0] = null;
                        cartesSobreLaTaula[1] = null;

                        if (maIA[0] == null && maIA[1] == null && maIA[2] == null) //no té cartes a la ma = final de partida
                        {
                            estat = "QuiGuanyaJoc";
                        }
                        else estat = "HRoba";
                        animacio1Feta = false;
                        CartaJAux.SetActive(false);
                        //CartaJ.SetActive(false);
                    }
                    break;
                case "IARoba":
                    //instr = "placeholder";
                    if (baralla.Count != 0)
                    {
                        switch (cartaTriada)
                        {
                            case 0: instr = "getC1"; break;
                            case 1: instr = "getC2"; break;
                            case 2: instr = "getC3"; break;
                            default: instr = "error"; break;
                        }
                        if (!animacio1Feta)
                        {
                            switch (cartaTriada)
                            {
                                case 0: CartaMa1.SetActive(true); break;
                                case 1: CartaMa2.SetActive(true); break;
                                case 2: CartaMa3.SetActive(true); break;
                            }
                            anim.Play(instr);
                            animacio1Feta = true;
                        }
                        if (!anim.IsPlaying(instr) && animacio1Feta)
                        {
                            maIA[cartaTriada] = baralla[0];
                            baralla.RemoveAt(0);

                            if (comencaH) //Si ha guanyat l'humà, ha robat primer. Ja podem començar el següent torn
                            {
                                estat = "EsperantH";
                            }
                            else //Si ha guanyat la IA, ha robat primer. Ara li toca robar a l'humà
                            {
                                estat = "HRoba";
                            }
                            animacio1Feta = false;
                            if (baralla.Count == 0)
                            {
                                CartaPinta.SetActive(false);
                            }
                        }
                    }
                    else
                    {
                        if (comencaH) //Si ha guanyat l'humà, ha robat primer. Ja podem començar el següent torn
                        {
                            estat = "EsperantH";
                        }
                        else //Si ha guanyat la IA, ha robat primer. Ara li toca robar a l'humà
                        {
                            estat = "HRoba";
                        }
                    }
                    break;
                case "HRoba":
                    if (baralla.Count != 0)
                    {
                        if (!animacio1Feta)
                        {
                            CartaJEntry.SetActive(true);
                            anim.Play("Hget");
                            animacio1Feta = true;
                        }
                        if (!anim.IsPlaying("Hget") && animacio1Feta)
                        {
                            maHuma[CartaTriadaH] = baralla[0];
                            baralla.RemoveAt(0);

                            if (comencaH) //Si ha guanyat l'humà, ha robat primer.  Ara li toca robar a la IA
                            {
                                estat = "IARoba";
                            }
                            else //Si ha guanyat la IA, ha robat primer. Ja podem començar el següent torn
                            {
                                estat = "IATria";
                            }
                            CartaTriadaH = -1;
                            animacio1Feta = false;
                            CartaJEntry.SetActive(false);
                            if (baralla.Count == 0)
                            {
                                CartaPinta.SetActive(false);
                            }
                        }
                    }
                    else
                    {
                        if (comencaH) //Si ha guanyat l'humà, ha robat primer.  Ara li toca robar a la IA
                        {
                            estat = "IARoba";
                        }
                        else //Si ha guanyat la IA, ha robat primer. Ja podem començar el següent torn
                        {
                            estat = "IATria";
                        }
                        CartaTriadaH = -1;
                    }
                    break;
                case "QuiGuanyaJoc":
                    if (!animacio1Feta) {
                        if (puntsIA > puntsH)
                        {
                            instr = "happy";
                            TextFinal.text = "ÌDERROTAÍ";
                            TextPuntsFinal.text = "ìPer!" + puntsIA.ToString() + "!punts!a!" + puntsH.ToString() + "í";
                            TextFinal.color = new Color(236.0f / 255.0f, 181.0f / 255.0f, 75.0f / 255.0f);
                            TextPuntsFinal.color = new Color(236.0f / 255.0f, 181.0f / 255.0f, 75.0f / 255.0f);
                            sortirDelJoc.GetComponentInChildren<Text>().color = new Color(236.0f / 255.0f, 181.0f / 255.0f, 75.0f / 255.0f);
                            s.Stop();
                            s.PlayOneShot(soVictoriaIA,1F);
                        } else
                        {
                            instr = "angry";
                            TextFinal.text = "ÌVICTORIAÍ";
                            TextPuntsFinal.text = "ìPer!" + puntsH.ToString() + "!punts!a!" + puntsIA.ToString() + "í";
                            TextFinal.color = new Color(140.0f / 255.0f, 185.0f / 255.0f, 66.0f / 255.0f);
                            TextPuntsFinal.color = new Color(140.0f / 255.0f, 185.0f / 255.0f, 66.0f / 255.0f);
                            sortirDelJoc.GetComponentInChildren<Text>().color = new Color(140.0f / 255.0f, 185.0f / 255.0f, 66.0f / 255.0f);
                            s.Stop();
                            s.PlayOneShot(soVictoriaH,1F); 
                        }
                        anim.Play(instr);
                        animacio1Feta = true;
                        panell.SetActive(true);
                        TextFinal.gameObject.SetActive(true);
                        TextPuntsFinal.gameObject.SetActive(true);
                        TextGeneral.gameObject.SetActive(false);
                        ButtStart.gameObject.SetActive(false);
                        TextInfo.gameObject.SetActive(false);
                    }
                    if (!anim.IsPlaying(instr) && animacio1Feta)
                    {
                        sortirDelJoc.gameObject.SetActive(true);
                    }
                    break;
                default:
                    pause = true;
                    break;
            }

            if (baralla.Count == 0 && pinta.num != 0)
            {
                baralla.Add(new Carta(pinta));
                pinta.num = 0;
                Pila.SetActive(false);
            }

            TextMaIA.text = "";
            foreach (Carta c in maIA)
            {
                if (c != null)
                {
                    TextMaIA.text = TextMaIA.text + c.num.ToString() + c.pal + "  ";
                }
                else { TextMaIA.text = TextMaIA.text + "null  "; }
            }
            if (pinta != null)
            {
                TextPinta.text = pinta.num.ToString() + pinta.pal;

                if (pinta.num != 0) TextPinta2.text = pinta.bonica();
                else
                {
                    string palBonic;
                    switch (pinta.pal)
                    {
                        case 'o':
                            palBonic = "Oros";
                            break;
                        case 'e':
                            palBonic = "Espases";
                            break;
                        case 'b':
                            palBonic = "Bastos";
                            break;
                        case 'c':
                            palBonic = "Copes";
                            break;
                        default:
                            palBonic = "error";
                            break;
                    }
                    TextPinta2.text = "- (" + palBonic + ")";
                }
            }
            //TextMaH
            TextMaH.text = "";
            foreach (Carta c in maHuma)
            {
                if (c != null)
                {
                    TextMaH.text = TextMaH.text + c.num.ToString() + c.pal + "  ";
                }
                else
                {
                    TextMaH.text = TextMaH.text + "null ";
                }
            }
            //TextCartesTaula
            TextCartesTaula.text = "";
            foreach (Carta c in cartesSobreLaTaula)
            {
                if (c != null)
                {
                    TextCartesTaula.text = TextCartesTaula.text + c.num.ToString() + c.pal + "  ";
                }
                else
                {
                    TextCartesTaula.text = TextCartesTaula.text + "null ";
                }
            }

            TextCartesTaula2.text = "";
            foreach (Carta c in cartesSobreLaTaula)
            {
                if (c != null)
                {
                    TextCartesTaula2.text += c.bonica() + "\n";
                }
                else
                {
                    TextCartesTaula2.text += "- \n";
                }
            }
            TextPuntsIA.text = puntsIA.ToString();
            TextPuntsH.text = puntsH.ToString();
            TextPila.text = baralla.Count.ToString();
            TextPila2.text = baralla.Count.ToString();

            if (maHuma[0] == null) ButtC1.gameObject.SetActive(false);
            else
            {
                ButtC1.gameObject.SetActive(true);
                //ìJUGAR!12!D’ESPASESí
                if (ButtC1.interactable)
                {
                    ButtC1.GetComponentInChildren<Text>().text = "ìJUGAR!UN!" + maHuma[0].bonicaBotons();
                    ButtC1.GetComponentInChildren<Text>().color = new Color(32.0f / 255.0f, 60.0f / 255.0f, 36.0f / 255.0f);
                }
                else
                {
                    ButtC1.GetComponentInChildren<Text>().text = "ì" + maHuma[0].bonicaBotons();
                    ButtC1.GetComponentInChildren<Text>().color = new Color(32.0f / 255.0f, 60.0f / 255.0f, 36.0f / 255.0f, 240.0f / 255.0f);
                }
            }
            if (maHuma[1] == null) ButtC2.gameObject.SetActive(false);
            else
            {
                ButtC2.gameObject.SetActive(true);

                if (ButtC2.interactable)
                {
                    ButtC2.GetComponentInChildren<Text>().text = "ìJUGAR!UN!" + maHuma[1].bonicaBotons();
                    ButtC2.GetComponentInChildren<Text>().color = new Color(32.0f / 255.0f, 60.0f / 255.0f, 36.0f / 255.0f);
                }
                else
                {
                    ButtC2.GetComponentInChildren<Text>().text = "ì" + maHuma[1].bonicaBotons();
                    ButtC2.GetComponentInChildren<Text>().color = new Color(32.0f / 255.0f, 60.0f / 255.0f, 36.0f / 255.0f, 240.0f / 255.0f);
                }
            }
            if (maHuma[2] == null) ButtC3.gameObject.SetActive(false);
            else
            {
                ButtC3.gameObject.SetActive(true);
                if (ButtC3.interactable)
                {
                    ButtC3.GetComponentInChildren<Text>().text = "ìJUGAR!UN!" + maHuma[2].bonicaBotons();
                    ButtC3.GetComponentInChildren<Text>().color = new Color(32.0f / 255.0f, 60.0f / 255.0f, 36.0f / 255.0f);
                }
                else {
                    ButtC3.GetComponentInChildren<Text>().text = "ì" + maHuma[2].bonicaBotons();
                    ButtC3.GetComponentInChildren<Text>().color = new Color(32.0f / 255.0f, 60.0f / 255.0f, 36.0f / 255.0f, 240.0f / 255.0f);
                }
            }
        }

    }

    //ButtC1.gameObject.SetActive(false);

    //baralla.RemoveAt(0); per fer pop!

    //Debug.Log("Abans de shuffle");
    //Debug.Log(baralla[0].num);
    //Debug.Log(baralla[0].pal);

    
    void OnClickStartPause()
    {
        if (pause){
            pause = false;
            float desp;
            if (ButtStart.GetComponentInChildren<Text>().text == "îjugarï") desp = 0;
            else desp = -25.3f;
            ButtStart.transform.position += new Vector3(desp, 0, 0);
            ButtStart.GetComponentInChildren<Text>().text = "îpausaï";
            sortirDelJoc.gameObject.SetActive(false);
        }
        else
        {
            pause = true;
            
            ButtStart.transform.position += new Vector3(25.3f, 0, 0);
            ButtStart.GetComponentInChildren<Text>().text = "îreprendreï";
            sortirDelJoc.gameObject.SetActive(true);
        }

    }

    void OnClickCarta(int c)
    {
        CartaTriadaH = c;
    }
}

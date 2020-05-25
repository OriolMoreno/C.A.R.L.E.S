using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class scriptAnim1 : MonoBehaviour
{
    public Animation anim;

    // Start is called before the first frame update
    void Start()
    {
        anim = GetComponent<Animation>();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Alpha1))
        {
            anim.Play("throwC1");
        }
        else if (Input.GetKeyDown(KeyCode.Alpha2))
        {
            anim.Play("throwC2");
        }
        else if (Input.GetKeyDown(KeyCode.Alpha3))
        {
            anim.Play("throwC3");
        }
        else if (Input.GetKeyDown(KeyCode.Alpha4))
        {
            anim.Play("getC1");
        }
        else if (Input.GetKeyDown(KeyCode.Alpha5))
        {
            anim.Play("getC2");
        }
        else if (Input.GetKeyDown(KeyCode.Alpha6))
        {
            anim.Play("getC3");
        }
        else if (Input.GetKeyDown(KeyCode.Alpha7))
        {
            anim.Play("recullCartes");
        }
        else if (Input.GetKeyDown(KeyCode.Alpha8))
        {
            anim.Play("happy");
        }
        else if (Input.GetKeyDown(KeyCode.Alpha9))
        {
            anim.Play("angry");
        }
        else if (Input.GetKeyDown(KeyCode.Q))
        {
            anim.Play("Hthrow");
        }
        else if (Input.GetKeyDown(KeyCode.W))
        {
            anim.Play("Hget");
        }
        else if (Input.GetKeyDown(KeyCode.E))
        {
            anim.Play("HRecullCartes");
        }
    }
}

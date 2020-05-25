using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class scriptAnim : MonoBehaviour
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
            anim.Play("clip1");
        }
        else if (Input.GetKeyDown(KeyCode.Alpha2))
        {
            anim.Play("clip2");
        }
    }
}

#include <stdio.h>

int main(int argc, char const *argv[])
{
    int w, i, f, frames[50];

    printf("please enter the wwindow size: \n");
    scanf("%d", &w);

    printf("enter the number of frames to transmit: \n");
    scanf("%d", &f);

    printf("enter %d frames individually: ", f);
    for (i = 1; i <= f; i++)
    {
        scanf("%d", &frames[i]);
    }

    printf("it uses sliding window protocol for a reliable and sequential delivery of data frames\n");

    for (i = 1; i <= f; i++)
    {
        if (i % w == 0)
        {
            printf("%d\t", frames[i]);
            printf("acknowledgement of above frames recieved by the sender\n");
        }
        else
        {
            printf("ack recieved %d\n", frames[i]);
        }
    }
    printf("\nacknowledgement of above frames recieved");
}

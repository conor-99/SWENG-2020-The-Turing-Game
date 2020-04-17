/* Reference: https://github.com/ScaleDrone/android-chat-tutorial */

package com.sweng.theturinggamedemo;

import android.app.Activity;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import org.w3c.dom.Text;

import java.util.ArrayList;
import java.util.List;

class MessageAdapter extends BaseAdapter {

    List<Message> messages = new ArrayList<Message>();
    private Context ctx;

    MessageAdapter(Context ctx) {
        this.ctx = ctx;
    }

    void add(Message message) {
        this.messages.add(message);
        notifyDataSetChanged();
    }

    @Override
    public int getCount() {
        return messages.size();
    }

    @Override
    public Object getItem(int i) {
        return messages.get(i);
    }

    @Override
    public long getItemId(int i) {
        return i;
    }

    @Override
    public View getView(int i, View convertView, ViewGroup viewGroup) {

        MessageViewHolder holder = new MessageViewHolder();
        LayoutInflater messageInflater = (LayoutInflater) ctx.getSystemService(Activity.LAYOUT_INFLATER_SERVICE);
        Message message = messages.get(i);

        if (message.ourMessage) {
            convertView = messageInflater.inflate(R.layout.message_us, null);
            holder.messageText = convertView.findViewById(R.id.message_body);
            convertView.setTag(holder);
            holder.messageText.setText(message.messageText);
        }
        else {
            convertView = messageInflater.inflate(R.layout.message_them, null);
            holder.messageText = convertView.findViewById(R.id.message_body);
            convertView.setTag(holder);
            holder.messageText.setText(message.messageText);
        }

        return convertView;

    }

}

class MessageViewHolder {
    TextView messageText;
}

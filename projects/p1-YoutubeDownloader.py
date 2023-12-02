import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from tkinter import messagebox as mb


def __main__():
    root = tk.Tk()
    root.title("Youtube Downloader")

    grid = tk.Frame(root, background="#212121")
    grid.grid(row=0, column=0, padx=1, pady=1)

    tx_link = tk.StringVar()

    tk.Label(grid, text="Enter Youtube link: ", background="#212121", foreground="#ffffff").grid(row=0, pady=5)
    tk.Entry(grid, textvariable=tx_link, width=50).grid(row=1, pady=5, padx=40)
    tk.Button(grid, text="SEARCH", command=lambda: start(tx_link.get(), grid),
              background="#c7000d", foreground="#ffffff").grid(row=2, pady=5)

    root.mainloop()


def start(link: str, grid: tk.Frame):
    try:
        yt_obj = YouTube(link)

        resFrame = tk.LabelFrame(grid, text=yt_obj.title, background="#212121", foreground="#ffffff")
        resFrame.grid(padx=10, pady=10, sticky=tk.NSEW)

        cb_selected_mp4 = tk.StringVar()
        cb_selected_webm = tk.StringVar()

        combobox_mp4 = ttk.Combobox(resFrame, textvariable=cb_selected_mp4)
        combobox_mp4.grid(padx=10, pady=5, column=0, row=0)
        combobox_webm = ttk.Combobox(resFrame, textvariable=cb_selected_webm)
        combobox_webm.grid(padx=10, pady=5, column=0, row=1)

        video_streams_mp4 = [stream for stream in yt_obj.streams if stream.mime_type.startswith('video/mp4')]
        video_streams_webm = [stream for stream in yt_obj.streams if stream.mime_type.startswith('video/webm')]

        resolutions = [stream.resolution for stream in video_streams_mp4]
        combobox_mp4['values'] = resolutions

        resolutions = [stream.resolution for stream in video_streams_webm]
        combobox_webm['values'] = resolutions

        tk.Button(resFrame, text="DOWNLOAD MP4", width=20, command=lambda: download_mp4(
            yt_obj, cb_selected_mp4.get())).grid(padx=10, pady=5, column=1, row=0)
        tk.Button(resFrame, text="DOWNLOAD WEBM", width=20, command=lambda: download_webm(
            yt_obj, cb_selected_webm.get())).grid(padx=10, pady=5, column=1, row=1)
    except Exception as e:
        mb.showerror("Download Error", e)


def download_mp4(yt: YouTube, selected_res: str):
    try:
        video = yt.streams.get_by_resolution(selected_res)
        video.download("videos", "yt_dl.mp4")
        mb.showinfo("Video Downloaded", f"""Title: {yt.title}
                    Location: {video.get_file_path("yt_dl.mp4", "videos")}
                    Filesize: {video.filesize_kb}kb
                    Resolution: {selected_res}""")
    except Exception as e:
        mb.showerror("Download Error", e)


def download_webm(yt: YouTube, selected_res: str):
    try:
        video = yt.streams.get_by_resolution(selected_res)
        video.download("videos", "yt_dl.webm")
        mb.showinfo("Video Downloaded", f"""Title: {yt.title}
                    Location: {video.get_file_path("yt_dl.webm", "videos")}
                    Filesize: {video.filesize_kb}kb
                    Resolution: {selected_res}""")
    except Exception as e:
        mb.showerror("Download Error", e)


if __name__ == "__main__":
    __main__()

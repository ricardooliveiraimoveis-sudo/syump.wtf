import os
from flask import Flask, render_template_string

app = Flask(__name__)

# Template HTML completo do Syump ServerSide (Estilo Alterion / Glassmorphism)
SYUMP_TEMPLATE = r"""
<!DOCTYPE html>
<html lang="en" class="font-sans">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Syump ServerSide — Roblox SS Executor</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root { --background: #050507; --theme-accent: #ffffff; }
        body { font-family: 'Inter', sans-serif; background-color: var(--background); color: #ffffff; }
        .glass-panel { background: linear-gradient(180deg, rgba(255,255,255,0.02) 0%, rgba(255,255,255,0.005) 100%); backdrop-filter: blur(12px); }
        .silver-shine { background: linear-gradient(180deg, #ffffff 0%, rgba(255,255,255,0.6) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .custom-scrollbar::-webkit-scrollbar { width: 4px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 4px; }
    </style>
</head>
<body class="min-h-screen bg-[#050507] text-white flex flex-col antialiased relative overflow-x-hidden">

    <!-- Background Grid Motes -->
    <div class="fixed inset-0 pointer-events-none z-0">
        <div class="absolute inset-0" style="background-image: linear-gradient(to right, rgba(255,255,255,0.02) 1px, transparent 1px), linear-gradient(to bottom, rgba(255,255,255,0.02) 1px, transparent 1px); background-size: 32px 32px;"></div>
        <div class="absolute top-1/3 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] rounded-full pointer-events-none" style="background: radial-gradient(rgba(255, 255, 255, 0.04) 0%, transparent 70%); filter: blur(100px);"></div>
    </div>

    <!-- MAIN DASHBOARD CONTAINER -->
    <div class="flex h-screen relative overflow-hidden z-10">
        
        <!-- SIDEBAR -->
        <aside class="flex flex-col w-[280px] z-50 fixed inset-y-0 left-0 bg-[#050507]/90 border-r border-white/[0.05] backdrop-blur-xl">
            <div class="flex flex-col items-center justify-center px-6 py-6 border-b border-white/[0.05]">
                <div class="flex items-center gap-3 font-bold text-lg tracking-tighter">
                    <div class="w-8 h-8 rounded-xl bg-white/10 flex items-center justify-center font-bold text-sm">S</div>
                    <span>Syump SS</span>
                </div>
            </div>

            <nav class="flex-1 px-3 py-4 space-y-1 overflow-y-auto custom-scrollbar">
                <p class="px-4 mb-3 text-[10.5px] text-white/35 uppercase tracking-wider font-semibold">Navigation</p>
                
                <a href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-xl bg-white/[0.06] border border-white/10 text-white transition-all">
                    <i class="fa-solid fa-house w-5 text-center text-xs"></i>
                    <span class="text-[13px] font-medium">Overview</span>
                </a>
                <a href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-white/60 hover:text-white hover:bg-white/[0.03] transition-all">
                    <i class="fa-solid fa-terminal w-5 text-center text-xs"></i>
                    <span class="text-[13px] font-medium">Server Explorer</span>
                </a>
                <a href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-white/60 hover:text-white hover:bg-white/[0.03] transition-all">
                    <i class="fa-solid fa-download w-5 text-center text-xs"></i>
                    <span class="text-[13px] font-medium">Loader & Scripts</span>
                </a>
                <a href="#" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-white/60 hover:text-white hover:bg-white/[0.03] transition-all">
                    <i class="fa-solid fa-gear w-5 text-center text-xs"></i>
                    <span class="text-[13px] font-medium">Settings</span>
                </a>
            </nav>

            <!-- User Profile Footer in Sidebar -->
            <div class="p-4 border-t border-white/[0.05]">
                <div class="p-3 bg-white/[0.03] border border-white/[0.05] rounded-xl flex items-center gap-3">
                    <div class="w-9 h-9 rounded-full bg-gradient-to-br from-slate-500 to-slate-700 flex items-center justify-center font-bold text-xs text-white">R</div>
                    <div class="flex-1 min-w-0">
                        <p class="text-xs font-semibold text-white truncate">ricardo_dev</p>
                        <span class="inline-block px-2 py-0.5 rounded-full bg-white/[0.05] text-[9px] uppercase tracking-wider text-slate-400">Developer</span>
                    </div>
                </div>
            </div>
        </aside>

        <!-- CONTENT AREA -->
        <div class="flex-1 flex flex-col min-w-0 ml-[280px]">
            
            <!-- HEADER -->
            <header class="h-14 flex items-center justify-between px-6 border-b border-white/[0.05] bg-transparent backdrop-blur-md">
                <div class="flex items-center gap-3 text-xs font-medium text-white/50">
                    <span>syump.wtf</span>
                    <i class="fa-solid fa-chevron-right text-[10px]"></i>
                    <span class="text-white font-semibold">Dashboard</span>
                </div>
                <div class="flex items-center gap-3">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
                    <span class="text-xs text-slate-400 font-medium">SS Gateway Active</span>
                </div>
            </header>

            <!-- MAIN VIEW -->
            <main class="flex-1 overflow-y-auto p-8 custom-scrollbar">
                <div class="max-w-5xl mx-auto space-y-8">
                    
                    <!-- Welcome Banner -->
                    <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 p-6 rounded-3xl glass-panel border border-white/10 shadow-2xl">
                        <div>
                            <div class="inline-block px-3 py-1 rounded-full bg-white/[0.05] border border-white/10 text-[10px] uppercase tracking-widest font-semibold mb-3 text-white/70">Syump ServerSide System</div>
                            <h1 class="text-3xl font-extrabold tracking-tight silver-shine">Control Center</h1>
                            <p class="text-xs text-white/50 mt-1">Manage server-side scripts, game hooks, and injection payloads securely.</p>
                        </div>
                        <a href="#" class="px-5 py-2.5 rounded-xl font-bold text-xs bg-white text-black hover:bg-slate-200 transition-all shadow-lg">
                            Copy Loader Script →
                        </a>
                    </div>

                    <!-- Grid Stats -->
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div class="p-5 rounded-2xl glass-panel border border-white/10">
                            <span class="text-[10px] text-white/
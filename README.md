# SyndProxy private pool

## Current pool

- Alive now: 1000
- Gold now: 389
- HTTP: 320 alive / 91 gold
- HTTPS: 240 alive / 34 gold
- SOCKS4: 206 alive / 136 gold
- SOCKS5: 234 alive / 128 gold

## Historical pool

- Discovered: 161986
- Ever alive: 31283
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

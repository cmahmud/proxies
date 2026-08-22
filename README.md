# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 440
- HTTP: 326 alive / 96 gold
- HTTPS: 220 alive / 33 gold
- SOCKS4: 209 alive / 140 gold
- SOCKS5: 260 alive / 171 gold

## Historical pool

- Discovered: 161986
- Ever alive: 31263
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

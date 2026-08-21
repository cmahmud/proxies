# SyndProxy private pool

## Current pool

- Alive now: 1145
- Gold now: 391
- HTTP: 370 alive / 109 gold
- HTTPS: 259 alive / 30 gold
- SOCKS4: 214 alive / 116 gold
- SOCKS5: 302 alive / 136 gold

## Historical pool

- Discovered: 152741
- Ever alive: 28022
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

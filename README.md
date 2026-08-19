# SyndProxy private pool

## Current pool

- Alive now: 1022
- Gold now: 515
- HTTP: 344 alive / 148 gold
- HTTPS: 264 alive / 92 gold
- SOCKS4: 214 alive / 148 gold
- SOCKS5: 200 alive / 127 gold

## Historical pool

- Discovered: 117156
- Ever alive: 17612
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 808
- Gold now: 336
- HTTP: 251 alive / 61 gold
- HTTPS: 155 alive / 13 gold
- SOCKS4: 209 alive / 144 gold
- SOCKS5: 193 alive / 118 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20148
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

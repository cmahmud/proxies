# SyndProxy private pool

## Current pool

- Alive now: 954
- Gold now: 344
- HTTP: 330 alive / 64 gold
- HTTPS: 219 alive / 13 gold
- SOCKS4: 207 alive / 141 gold
- SOCKS5: 198 alive / 126 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20236
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

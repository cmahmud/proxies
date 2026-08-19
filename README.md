# SyndProxy private pool

## Current pool

- Alive now: 908
- Gold now: 344
- HTTP: 302 alive / 64 gold
- HTTPS: 196 alive / 13 gold
- SOCKS4: 213 alive / 140 gold
- SOCKS5: 197 alive / 127 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20221
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

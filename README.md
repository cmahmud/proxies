# SyndProxy private pool

## Current pool

- Alive now: 889
- Gold now: 259
- HTTP: 300 alive / 28 gold
- HTTPS: 155 alive / 3 gold
- SOCKS4: 210 alive / 118 gold
- SOCKS5: 224 alive / 110 gold

## Historical pool

- Discovered: 99142
- Ever alive: 12063
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

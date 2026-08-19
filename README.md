# SyndProxy private pool

## Current pool

- Alive now: 925
- Gold now: 332
- HTTP: 318 alive / 64 gold
- HTTPS: 179 alive / 13 gold
- SOCKS4: 207 alive / 125 gold
- SOCKS5: 221 alive / 130 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20124
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

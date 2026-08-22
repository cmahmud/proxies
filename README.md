# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 379
- HTTP: 304 alive / 86 gold
- HTTPS: 193 alive / 21 gold
- SOCKS4: 198 alive / 115 gold
- SOCKS5: 255 alive / 157 gold

## Historical pool

- Discovered: 166337
- Ever alive: 32400
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

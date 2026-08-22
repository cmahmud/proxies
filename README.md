# SyndProxy private pool

## Current pool

- Alive now: 858
- Gold now: 385
- HTTP: 274 alive / 86 gold
- HTTPS: 151 alive / 21 gold
- SOCKS4: 178 alive / 116 gold
- SOCKS5: 255 alive / 162 gold

## Historical pool

- Discovered: 166337
- Ever alive: 32396
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

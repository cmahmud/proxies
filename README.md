# SyndProxy private pool

## Current pool

- Alive now: 752
- Gold now: 387
- HTTP: 178 alive / 79 gold
- HTTPS: 156 alive / 26 gold
- SOCKS4: 204 alive / 127 gold
- SOCKS5: 214 alive / 155 gold

## Historical pool

- Discovered: 150519
- Ever alive: 27066
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 899
- Gold now: 341
- HTTP: 334 alive / 89 gold
- HTTPS: 161 alive / 30 gold
- SOCKS4: 163 alive / 96 gold
- SOCKS5: 241 alive / 126 gold

## Historical pool

- Discovered: 167408
- Ever alive: 32568
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

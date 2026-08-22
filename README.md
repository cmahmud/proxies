# SyndProxy private pool

## Current pool

- Alive now: 990
- Gold now: 368
- HTTP: 345 alive / 76 gold
- HTTPS: 213 alive / 26 gold
- SOCKS4: 214 alive / 137 gold
- SOCKS5: 218 alive / 129 gold

## Historical pool

- Discovered: 165836
- Ever alive: 32360
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

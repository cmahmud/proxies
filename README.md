# SyndProxy private pool

## Current pool

- Alive now: 942
- Gold now: 408
- HTTP: 266 alive / 82 gold
- HTTPS: 206 alive / 23 gold
- SOCKS4: 216 alive / 152 gold
- SOCKS5: 254 alive / 151 gold

## Historical pool

- Discovered: 165845
- Ever alive: 32372
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

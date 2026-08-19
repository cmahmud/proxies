# SyndProxy private pool

## Current pool

- Alive now: 984
- Gold now: 366
- HTTP: 316 alive / 78 gold
- HTTPS: 222 alive / 13 gold
- SOCKS4: 217 alive / 126 gold
- SOCKS5: 229 alive / 149 gold

## Historical pool

- Discovered: 129304
- Ever alive: 20389
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

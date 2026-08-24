# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 386
- HTTP: 89 alive / 53 gold
- HTTPS: 56 alive / 14 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 186 alive / 161 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33485
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

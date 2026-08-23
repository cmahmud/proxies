# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 373
- HTTP: 101 alive / 47 gold
- HTTPS: 37 alive / 12 gold
- SOCKS4: 167 alive / 155 gold
- SOCKS5: 188 alive / 159 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32959
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

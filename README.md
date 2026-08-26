# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 410
- HTTP: 98 alive / 63 gold
- HTTPS: 97 alive / 19 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 189 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38433
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

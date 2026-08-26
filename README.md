# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 371
- HTTP: 98 alive / 61 gold
- HTTPS: 51 alive / 17 gold
- SOCKS4: 151 alive / 144 gold
- SOCKS5: 167 alive / 149 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38866
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

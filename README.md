# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 381
- HTTP: 115 alive / 68 gold
- HTTPS: 73 alive / 18 gold
- SOCKS4: 153 alive / 142 gold
- SOCKS5: 178 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38782
- Ever gold: 1292

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

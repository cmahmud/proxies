# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 397
- HTTP: 100 alive / 66 gold
- HTTPS: 78 alive / 18 gold
- SOCKS4: 164 alive / 157 gold
- SOCKS5: 168 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37427
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

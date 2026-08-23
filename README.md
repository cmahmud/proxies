# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 355
- HTTP: 81 alive / 32 gold
- HTTPS: 53 alive / 10 gold
- SOCKS4: 165 alive / 154 gold
- SOCKS5: 179 alive / 159 gold

## Historical pool

- Discovered: 171794
- Ever alive: 32946
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

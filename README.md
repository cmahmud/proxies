# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 389
- HTTP: 89 alive / 51 gold
- HTTPS: 52 alive / 12 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33554
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

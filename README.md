# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 423
- HTTP: 100 alive / 63 gold
- HTTPS: 105 alive / 22 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 208 alive / 177 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35913
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

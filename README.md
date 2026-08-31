# SyndProxy validated proxy pool

## Current pool

- Alive now: 681
- Gold now: 471
- HTTP: 170 alive / 97 gold
- HTTPS: 118 alive / 35 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 222 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45289
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

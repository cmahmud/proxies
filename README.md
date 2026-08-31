# SyndProxy validated proxy pool

## Current pool

- Alive now: 679
- Gold now: 471
- HTTP: 169 alive / 97 gold
- HTTPS: 113 alive / 38 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 220 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45307
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

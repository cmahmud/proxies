# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 438
- HTTP: 125 alive / 80 gold
- HTTPS: 96 alive / 27 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 205 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45460
- Ever gold: 1432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

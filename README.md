# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 471
- HTTP: 123 alive / 97 gold
- HTTPS: 114 alive / 40 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 192 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44845
- Ever gold: 1415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

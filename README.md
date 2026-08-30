# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 424
- HTTP: 134 alive / 81 gold
- HTTPS: 82 alive / 32 gold
- SOCKS4: 159 alive / 151 gold
- SOCKS5: 246 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43934
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

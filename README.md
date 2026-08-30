# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 423
- HTTP: 124 alive / 84 gold
- HTTPS: 95 alive / 29 gold
- SOCKS4: 160 alive / 151 gold
- SOCKS5: 188 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44036
- Ever gold: 1391

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

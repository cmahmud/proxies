# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 433
- HTTP: 122 alive / 89 gold
- HTTPS: 82 alive / 34 gold
- SOCKS4: 162 alive / 151 gold
- SOCKS5: 180 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44074
- Ever gold: 1396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

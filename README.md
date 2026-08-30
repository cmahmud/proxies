# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 446
- HTTP: 119 alive / 81 gold
- HTTPS: 135 alive / 38 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44739
- Ever gold: 1412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

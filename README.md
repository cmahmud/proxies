# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 441
- HTTP: 121 alive / 82 gold
- HTTPS: 76 alive / 33 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44296
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

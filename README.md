# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 446
- HTTP: 139 alive / 87 gold
- HTTPS: 74 alive / 34 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 206 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44234
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

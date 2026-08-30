# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 448
- HTTP: 124 alive / 89 gold
- HTTPS: 67 alive / 36 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 201 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44262
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 441
- HTTP: 120 alive / 85 gold
- HTTPS: 70 alive / 34 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 201 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44148
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

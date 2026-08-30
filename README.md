# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 473
- HTTP: 133 alive / 95 gold
- HTTPS: 104 alive / 41 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 200 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44924
- Ever gold: 1419

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

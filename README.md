# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 432
- HTTP: 123 alive / 88 gold
- HTTPS: 78 alive / 32 gold
- SOCKS4: 159 alive / 153 gold
- SOCKS5: 172 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44079
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

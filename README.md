# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 413
- HTTP: 94 alive / 59 gold
- HTTPS: 67 alive / 23 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45504
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

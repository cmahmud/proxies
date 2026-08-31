# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 413
- HTTP: 102 alive / 58 gold
- HTTPS: 80 alive / 27 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 190 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45515
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

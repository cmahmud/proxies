# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 413
- HTTP: 89 alive / 59 gold
- HTTPS: 64 alive / 23 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45517
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

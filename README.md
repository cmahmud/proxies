# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 413
- HTTP: 112 alive / 58 gold
- HTTPS: 71 alive / 23 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 194 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45518
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

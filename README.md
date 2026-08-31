# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 411
- HTTP: 92 alive / 58 gold
- HTTPS: 68 alive / 23 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45505
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

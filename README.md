# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 445
- HTTP: 135 alive / 92 gold
- HTTPS: 76 alive / 34 gold
- SOCKS4: 166 alive / 157 gold
- SOCKS5: 206 alive / 162 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44250
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

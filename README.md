# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 423
- HTTP: 132 alive / 82 gold
- HTTPS: 79 alive / 31 gold
- SOCKS4: 156 alive / 151 gold
- SOCKS5: 233 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43951
- Ever gold: 1381

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 447
- HTTP: 128 alive / 80 gold
- HTTPS: 125 alive / 35 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44651
- Ever gold: 1409

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 447
- HTTP: 116 alive / 81 gold
- HTTPS: 120 alive / 35 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44649
- Ever gold: 1409

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

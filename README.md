# SyndProxy validated proxy pool

## Current pool

- Alive now: 415
- Gold now: 342
- HTTP: 81 alive / 60 gold
- HTTPS: 29 alive / 15 gold
- SOCKS4: 146 alive / 135 gold
- SOCKS5: 159 alive / 132 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48389
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 415
- Gold now: 328
- HTTP: 87 alive / 63 gold
- HTTPS: 40 alive / 12 gold
- SOCKS4: 144 alive / 132 gold
- SOCKS5: 144 alive / 121 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48363
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

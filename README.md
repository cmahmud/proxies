# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 394
- HTTP: 96 alive / 64 gold
- HTTPS: 47 alive / 15 gold
- SOCKS4: 170 alive / 155 gold
- SOCKS5: 182 alive / 160 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48141
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 394
- HTTP: 93 alive / 61 gold
- HTTPS: 44 alive / 18 gold
- SOCKS4: 180 alive / 157 gold
- SOCKS5: 178 alive / 158 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48159
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

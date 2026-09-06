# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 396
- HTTP: 130 alive / 80 gold
- HTTPS: 62 alive / 25 gold
- SOCKS4: 164 alive / 139 gold
- SOCKS5: 180 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48037
- Ever gold: 1514

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

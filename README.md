# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 383
- HTTP: 95 alive / 64 gold
- HTTPS: 41 alive / 13 gold
- SOCKS4: 177 alive / 154 gold
- SOCKS5: 180 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48109
- Ever gold: 1519

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

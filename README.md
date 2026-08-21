# SyndProxy private pool

## Current pool

- Alive now: 762
- Gold now: 392
- HTTP: 242 alive / 90 gold
- HTTPS: 108 alive / 25 gold
- SOCKS4: 182 alive / 121 gold
- SOCKS5: 230 alive / 156 gold

## Historical pool

- Discovered: 156418
- Ever alive: 29469
- Ever gold: 1128

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

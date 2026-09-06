# SyndProxy validated proxy pool

## Current pool

- Alive now: 465
- Gold now: 384
- HTTP: 95 alive / 66 gold
- HTTPS: 40 alive / 15 gold
- SOCKS4: 162 alive / 151 gold
- SOCKS5: 168 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48205
- Ever gold: 1523

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

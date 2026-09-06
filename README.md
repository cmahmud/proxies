# SyndProxy validated proxy pool

## Current pool

- Alive now: 461
- Gold now: 380
- HTTP: 78 alive / 53 gold
- HTTPS: 32 alive / 14 gold
- SOCKS4: 171 alive / 156 gold
- SOCKS5: 180 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48317
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

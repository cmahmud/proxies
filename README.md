# SyndProxy validated proxy pool

## Current pool

- Alive now: 465
- Gold now: 378
- HTTP: 80 alive / 52 gold
- HTTPS: 34 alive / 14 gold
- SOCKS4: 171 alive / 156 gold
- SOCKS5: 180 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48318
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

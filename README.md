# SyndProxy private pool

## Current pool

- Alive now: 1247
- Gold now: 517
- HTTP: 488 alive / 190 gold
- HTTPS: 322 alive / 46 gold
- SOCKS4: 198 alive / 121 gold
- SOCKS5: 239 alive / 160 gold

## Historical pool

- Discovered: 125606
- Ever alive: 19578
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

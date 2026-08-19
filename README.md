# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 366
- HTTP: 344 alive / 67 gold
- HTTPS: 177 alive / 18 gold
- SOCKS4: 248 alive / 154 gold
- SOCKS5: 212 alive / 127 gold

## Historical pool

- Discovered: 110866
- Ever alive: 16021
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

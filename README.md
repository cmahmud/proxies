# SyndProxy private pool

## Current pool

- Alive now: 962
- Gold now: 366
- HTTP: 311 alive / 71 gold
- HTTPS: 187 alive / 15 gold
- SOCKS4: 252 alive / 154 gold
- SOCKS5: 212 alive / 126 gold

## Historical pool

- Discovered: 110866
- Ever alive: 16031
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

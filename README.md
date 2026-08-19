# SyndProxy private pool

## Current pool

- Alive now: 961
- Gold now: 356
- HTTP: 318 alive / 69 gold
- HTTPS: 182 alive / 18 gold
- SOCKS4: 250 alive / 153 gold
- SOCKS5: 211 alive / 116 gold

## Historical pool

- Discovered: 110866
- Ever alive: 16021
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

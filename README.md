# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 360
- HTTP: 323 alive / 64 gold
- HTTPS: 176 alive / 15 gold
- SOCKS4: 252 alive / 156 gold
- SOCKS5: 230 alive / 125 gold

## Historical pool

- Discovered: 110866
- Ever alive: 16024
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

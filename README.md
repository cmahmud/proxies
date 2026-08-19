# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 365
- HTTP: 323 alive / 69 gold
- HTTPS: 220 alive / 15 gold
- SOCKS4: 257 alive / 153 gold
- SOCKS5: 229 alive / 128 gold

## Historical pool

- Discovered: 110866
- Ever alive: 16031
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

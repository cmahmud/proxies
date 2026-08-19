# SyndProxy private pool

## Current pool

- Alive now: 1078
- Gold now: 510
- HTTP: 385 alive / 148 gold
- HTTPS: 271 alive / 89 gold
- SOCKS4: 193 alive / 118 gold
- SOCKS5: 229 alive / 155 gold

## Historical pool

- Discovered: 118126
- Ever alive: 17808
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 915
- Gold now: 301
- HTTP: 318 alive / 66 gold
- HTTPS: 233 alive / 18 gold
- SOCKS4: 194 alive / 117 gold
- SOCKS5: 170 alive / 100 gold

## Historical pool

- Discovered: 109991
- Ever alive: 15649
- Ever gold: 499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

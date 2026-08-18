# SyndProxy private pool

## Current pool

- Alive now: 983
- Gold now: 369
- HTTP: 292 alive / 61 gold
- HTTPS: 237 alive / 14 gold
- SOCKS4: 233 alive / 152 gold
- SOCKS5: 221 alive / 142 gold

## Historical pool

- Discovered: 109324
- Ever alive: 15178
- Ever gold: 488

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

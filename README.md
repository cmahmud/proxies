# SyndProxy private pool

## Current pool

- Alive now: 858
- Gold now: 395
- HTTP: 253 alive / 93 gold
- HTTPS: 185 alive / 24 gold
- SOCKS4: 212 alive / 145 gold
- SOCKS5: 208 alive / 133 gold

## Historical pool

- Discovered: 165825
- Ever alive: 32344
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

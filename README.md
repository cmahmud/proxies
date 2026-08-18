# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 321
- HTTP: 277 alive / 34 gold
- HTTPS: 198 alive / 10 gold
- SOCKS4: 237 alive / 144 gold
- SOCKS5: 233 alive / 133 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14209
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

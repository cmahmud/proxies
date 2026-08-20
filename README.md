# SyndProxy private pool

## Current pool

- Alive now: 1421
- Gold now: 588
- HTTP: 504 alive / 196 gold
- HTTPS: 435 alive / 89 gold
- SOCKS4: 236 alive / 144 gold
- SOCKS5: 246 alive / 159 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24042
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

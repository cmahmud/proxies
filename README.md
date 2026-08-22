# SyndProxy private pool

## Current pool

- Alive now: 920
- Gold now: 387
- HTTP: 259 alive / 90 gold
- HTTPS: 206 alive / 25 gold
- SOCKS4: 216 alive / 142 gold
- SOCKS5: 239 alive / 130 gold

## Historical pool

- Discovered: 163276
- Ever alive: 31791
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

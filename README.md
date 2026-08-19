# SyndProxy private pool

## Current pool

- Alive now: 1179
- Gold now: 381
- HTTP: 393 alive / 95 gold
- HTTPS: 256 alive / 12 gold
- SOCKS4: 238 alive / 138 gold
- SOCKS5: 292 alive / 136 gold

## Historical pool

- Discovered: 131826
- Ever alive: 21010
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

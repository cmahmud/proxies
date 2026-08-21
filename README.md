# SyndProxy private pool

## Current pool

- Alive now: 980
- Gold now: 364
- HTTP: 318 alive / 85 gold
- HTTPS: 230 alive / 19 gold
- SOCKS4: 201 alive / 124 gold
- SOCKS5: 231 alive / 136 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29834
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1073
- Gold now: 409
- HTTP: 369 alive / 95 gold
- HTTPS: 255 alive / 31 gold
- SOCKS4: 211 alive / 147 gold
- SOCKS5: 238 alive / 136 gold

## Historical pool

- Discovered: 160997
- Ever alive: 30969
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

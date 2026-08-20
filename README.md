# SyndProxy private pool

## Current pool

- Alive now: 1282
- Gold now: 565
- HTTP: 488 alive / 190 gold
- HTTPS: 355 alive / 94 gold
- SOCKS4: 215 alive / 147 gold
- SOCKS5: 224 alive / 134 gold

## Historical pool

- Discovered: 137899
- Ever alive: 22938
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1129
- Gold now: 426
- HTTP: 364 alive / 96 gold
- HTTPS: 285 alive / 25 gold
- SOCKS4: 221 alive / 144 gold
- SOCKS5: 259 alive / 161 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28201
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

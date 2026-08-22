# SyndProxy private pool

## Current pool

- Alive now: 1012
- Gold now: 409
- HTTP: 369 alive / 93 gold
- HTTPS: 224 alive / 36 gold
- SOCKS4: 187 alive / 125 gold
- SOCKS5: 232 alive / 155 gold

## Historical pool

- Discovered: 163245
- Ever alive: 31704
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1004
- Gold now: 409
- HTTP: 358 alive / 92 gold
- HTTPS: 223 alive / 37 gold
- SOCKS4: 190 alive / 125 gold
- SOCKS5: 233 alive / 155 gold

## Historical pool

- Discovered: 163245
- Ever alive: 31705
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

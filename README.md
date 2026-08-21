# SyndProxy private pool

## Current pool

- Alive now: 928
- Gold now: 396
- HTTP: 296 alive / 94 gold
- HTTPS: 177 alive / 24 gold
- SOCKS4: 196 alive / 135 gold
- SOCKS5: 259 alive / 143 gold

## Historical pool

- Discovered: 154713
- Ever alive: 29004
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

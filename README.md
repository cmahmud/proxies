# SyndProxy private pool

## Current pool

- Alive now: 764
- Gold now: 369
- HTTP: 227 alive / 68 gold
- HTTPS: 135 alive / 16 gold
- SOCKS4: 210 alive / 149 gold
- SOCKS5: 192 alive / 136 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25487
- Ever gold: 1061

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

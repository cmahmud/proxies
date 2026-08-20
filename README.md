# SyndProxy private pool

## Current pool

- Alive now: 766
- Gold now: 381
- HTTP: 213 alive / 78 gold
- HTTPS: 124 alive / 20 gold
- SOCKS4: 226 alive / 147 gold
- SOCKS5: 203 alive / 136 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25490
- Ever gold: 1061

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

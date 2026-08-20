# SyndProxy private pool

## Current pool

- Alive now: 771
- Gold now: 377
- HTTP: 234 alive / 74 gold
- HTTPS: 134 alive / 20 gold
- SOCKS4: 210 alive / 149 gold
- SOCKS5: 193 alive / 134 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25487
- Ever gold: 1061

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

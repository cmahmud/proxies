# SyndProxy private pool

## Current pool

- Alive now: 756
- Gold now: 372
- HTTP: 221 alive / 71 gold
- HTTPS: 135 alive / 18 gold
- SOCKS4: 207 alive / 149 gold
- SOCKS5: 193 alive / 134 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25487
- Ever gold: 1061

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

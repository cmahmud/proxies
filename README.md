# SyndProxy private pool

## Current pool

- Alive now: 760
- Gold now: 381
- HTTP: 206 alive / 78 gold
- HTTPS: 139 alive / 20 gold
- SOCKS4: 216 alive / 147 gold
- SOCKS5: 199 alive / 136 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25489
- Ever gold: 1061

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

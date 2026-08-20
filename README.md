# SyndProxy private pool

## Current pool

- Alive now: 817
- Gold now: 412
- HTTP: 223 alive / 74 gold
- HTTPS: 139 alive / 20 gold
- SOCKS4: 225 alive / 156 gold
- SOCKS5: 230 alive / 162 gold

## Historical pool

- Discovered: 148329
- Ever alive: 26032
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

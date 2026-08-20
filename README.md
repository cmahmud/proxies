# SyndProxy private pool

## Current pool

- Alive now: 1061
- Gold now: 395
- HTTP: 323 alive / 98 gold
- HTTPS: 260 alive / 27 gold
- SOCKS4: 235 alive / 133 gold
- SOCKS5: 243 alive / 137 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25116
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

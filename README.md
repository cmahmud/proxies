# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 401
- HTTP: 367 alive / 86 gold
- HTTPS: 200 alive / 31 gold
- SOCKS4: 213 alive / 146 gold
- SOCKS5: 231 alive / 138 gold

## Historical pool

- Discovered: 167118
- Ever alive: 32530
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

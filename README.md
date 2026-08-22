# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 405
- HTTP: 392 alive / 89 gold
- HTTPS: 199 alive / 31 gold
- SOCKS4: 214 alive / 147 gold
- SOCKS5: 227 alive / 138 gold

## Historical pool

- Discovered: 167118
- Ever alive: 32530
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

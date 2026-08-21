# SyndProxy private pool

## Current pool

- Alive now: 1068
- Gold now: 431
- HTTP: 354 alive / 115 gold
- HTTPS: 215 alive / 28 gold
- SOCKS4: 247 alive / 147 gold
- SOCKS5: 252 alive / 141 gold

## Historical pool

- Discovered: 160279
- Ever alive: 30795
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

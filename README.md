# SyndProxy private pool

## Current pool

- Alive now: 922
- Gold now: 473
- HTTP: 294 alive / 127 gold
- HTTPS: 230 alive / 86 gold
- SOCKS4: 210 alive / 143 gold
- SOCKS5: 188 alive / 117 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17477
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

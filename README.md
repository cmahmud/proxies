# SyndProxy private pool

## Current pool

- Alive now: 1514
- Gold now: 619
- HTTP: 564 alive / 215 gold
- HTTPS: 503 alive / 119 gold
- SOCKS4: 227 alive / 150 gold
- SOCKS5: 220 alive / 135 gold

## Historical pool

- Discovered: 140473
- Ever alive: 23757
- Ever gold: 956

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1432
- Gold now: 611
- HTTP: 523 alive / 214 gold
- HTTPS: 410 alive / 111 gold
- SOCKS4: 233 alive / 150 gold
- SOCKS5: 266 alive / 136 gold

## Historical pool

- Discovered: 140466
- Ever alive: 23711
- Ever gold: 956

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1449
- Gold now: 628
- HTTP: 523 alive / 233 gold
- HTTPS: 444 alive / 112 gold
- SOCKS4: 217 alive / 142 gold
- SOCKS5: 265 alive / 141 gold

## Historical pool

- Discovered: 142747
- Ever alive: 24620
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

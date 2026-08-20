# SyndProxy private pool

## Current pool

- Alive now: 1487
- Gold now: 628
- HTTP: 548 alive / 234 gold
- HTTPS: 453 alive / 111 gold
- SOCKS4: 218 alive / 142 gold
- SOCKS5: 268 alive / 141 gold

## Historical pool

- Discovered: 142747
- Ever alive: 24619
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1499
- Gold now: 605
- HTTP: 562 alive / 218 gold
- HTTPS: 483 alive / 116 gold
- SOCKS4: 219 alive / 133 gold
- SOCKS5: 235 alive / 138 gold

## Historical pool

- Discovered: 140473
- Ever alive: 23774
- Ever gold: 960

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1592
- Gold now: 605
- HTTP: 561 alive / 208 gold
- HTTPS: 470 alive / 115 gold
- SOCKS4: 219 alive / 147 gold
- SOCKS5: 342 alive / 135 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23677
- Ever gold: 954

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

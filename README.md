# SyndProxy private pool

## Current pool

- Alive now: 1671
- Gold now: 635
- HTTP: 706 alive / 236 gold
- HTTPS: 516 alive / 134 gold
- SOCKS4: 185 alive / 103 gold
- SOCKS5: 264 alive / 162 gold

## Historical pool

- Discovered: 143423
- Ever alive: 24684
- Ever gold: 1032

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

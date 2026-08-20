# SyndProxy private pool

## Current pool

- Alive now: 1639
- Gold now: 634
- HTTP: 693 alive / 236 gold
- HTTPS: 515 alive / 133 gold
- SOCKS4: 184 alive / 103 gold
- SOCKS5: 247 alive / 162 gold

## Historical pool

- Discovered: 143423
- Ever alive: 24684
- Ever gold: 1032

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

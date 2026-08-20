# SyndProxy private pool

## Current pool

- Alive now: 1661
- Gold now: 637
- HTTP: 662 alive / 238 gold
- HTTPS: 511 alive / 113 gold
- SOCKS4: 217 alive / 142 gold
- SOCKS5: 271 alive / 144 gold

## Historical pool

- Discovered: 142746
- Ever alive: 24607
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

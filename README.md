# SyndProxy private pool

## Current pool

- Alive now: 660
- Gold now: 358
- HTTP: 177 alive / 69 gold
- HTTPS: 106 alive / 19 gold
- SOCKS4: 179 alive / 126 gold
- SOCKS5: 198 alive / 144 gold

## Historical pool

- Discovered: 146125
- Ever alive: 25599
- Ever gold: 1067

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

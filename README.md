# SyndProxy private pool

## Current pool

- Alive now: 1552
- Gold now: 640
- HTTP: 581 alive / 240 gold
- HTTPS: 492 alive / 113 gold
- SOCKS4: 215 alive / 143 gold
- SOCKS5: 264 alive / 144 gold

## Historical pool

- Discovered: 142746
- Ever alive: 24610
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

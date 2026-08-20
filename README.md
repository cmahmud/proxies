# SyndProxy private pool

## Current pool

- Alive now: 647
- Gold now: 360
- HTTP: 177 alive / 72 gold
- HTTPS: 93 alive / 20 gold
- SOCKS4: 180 alive / 124 gold
- SOCKS5: 197 alive / 144 gold

## Historical pool

- Discovered: 146125
- Ever alive: 25597
- Ever gold: 1067

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

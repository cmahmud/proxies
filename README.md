# SyndProxy private pool

## Current pool

- Alive now: 655
- Gold now: 360
- HTTP: 175 alive / 71 gold
- HTTPS: 102 alive / 19 gold
- SOCKS4: 174 alive / 126 gold
- SOCKS5: 204 alive / 144 gold

## Historical pool

- Discovered: 146125
- Ever alive: 25602
- Ever gold: 1067

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

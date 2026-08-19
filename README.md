# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 531
- HTTP: 360 alive / 153 gold
- HTTPS: 240 alive / 88 gold
- SOCKS4: 211 alive / 150 gold
- SOCKS5: 209 alive / 140 gold

## Historical pool

- Discovered: 119811
- Ever alive: 18038
- Ever gold: 712

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

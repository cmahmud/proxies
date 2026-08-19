# SyndProxy private pool

## Current pool

- Alive now: 872
- Gold now: 330
- HTTP: 285 alive / 63 gold
- HTTPS: 171 alive / 12 gold
- SOCKS4: 205 alive / 125 gold
- SOCKS5: 211 alive / 130 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20125
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

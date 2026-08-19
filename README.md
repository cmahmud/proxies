# SyndProxy private pool

## Current pool

- Alive now: 892
- Gold now: 320
- HTTP: 287 alive / 56 gold
- HTTPS: 192 alive / 11 gold
- SOCKS4: 203 alive / 124 gold
- SOCKS5: 210 alive / 129 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20128
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

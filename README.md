# SyndProxy private pool

## Current pool

- Alive now: 877
- Gold now: 330
- HTTP: 290 alive / 64 gold
- HTTPS: 174 alive / 12 gold
- SOCKS4: 203 alive / 125 gold
- SOCKS5: 210 alive / 129 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20125
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

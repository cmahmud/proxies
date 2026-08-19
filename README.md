# SyndProxy private pool

## Current pool

- Alive now: 844
- Gold now: 322
- HTTP: 263 alive / 58 gold
- HTTPS: 177 alive / 11 gold
- SOCKS4: 195 alive / 126 gold
- SOCKS5: 209 alive / 127 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20057
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

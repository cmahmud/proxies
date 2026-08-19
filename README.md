# SyndProxy private pool

## Current pool

- Alive now: 903
- Gold now: 324
- HTTP: 314 alive / 58 gold
- HTTPS: 173 alive / 10 gold
- SOCKS4: 210 alive / 127 gold
- SOCKS5: 206 alive / 129 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20126
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

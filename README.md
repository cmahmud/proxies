# SyndProxy private pool

## Current pool

- Alive now: 883
- Gold now: 328
- HTTP: 299 alive / 61 gold
- HTTPS: 167 alive / 9 gold
- SOCKS4: 211 alive / 126 gold
- SOCKS5: 206 alive / 132 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20126
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

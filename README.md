# SyndProxy private pool

## Current pool

- Alive now: 918
- Gold now: 323
- HTTP: 319 alive / 57 gold
- HTTPS: 178 alive / 10 gold
- SOCKS4: 215 alive / 127 gold
- SOCKS5: 206 alive / 129 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20126
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

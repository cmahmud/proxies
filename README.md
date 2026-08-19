# SyndProxy private pool

## Current pool

- Alive now: 825
- Gold now: 323
- HTTP: 248 alive / 61 gold
- HTTPS: 172 alive / 15 gold
- SOCKS4: 197 alive / 126 gold
- SOCKS5: 208 alive / 121 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20063
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

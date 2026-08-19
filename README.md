# SyndProxy private pool

## Current pool

- Alive now: 895
- Gold now: 322
- HTTP: 304 alive / 55 gold
- HTTPS: 172 alive / 12 gold
- SOCKS4: 213 alive / 125 gold
- SOCKS5: 206 alive / 130 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20126
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

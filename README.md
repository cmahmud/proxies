# SyndProxy private pool

## Current pool

- Alive now: 889
- Gold now: 316
- HTTP: 308 alive / 54 gold
- HTTPS: 183 alive / 10 gold
- SOCKS4: 193 alive / 126 gold
- SOCKS5: 205 alive / 126 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20047
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 847
- Gold now: 320
- HTTP: 282 alive / 57 gold
- HTTPS: 173 alive / 12 gold
- SOCKS4: 188 alive / 126 gold
- SOCKS5: 204 alive / 125 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20047
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

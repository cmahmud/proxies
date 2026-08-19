# SyndProxy private pool

## Current pool

- Alive now: 886
- Gold now: 320
- HTTP: 285 alive / 62 gold
- HTTPS: 166 alive / 14 gold
- SOCKS4: 204 alive / 125 gold
- SOCKS5: 231 alive / 119 gold

## Historical pool

- Discovered: 129246
- Ever alive: 20093
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 746
- Gold now: 401
- HTTP: 177 alive / 93 gold
- HTTPS: 127 alive / 20 gold
- SOCKS4: 218 alive / 138 gold
- SOCKS5: 224 alive / 150 gold

## Historical pool

- Discovered: 154732
- Ever alive: 29176
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

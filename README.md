# SyndProxy private pool

## Current pool

- Alive now: 917
- Gold now: 400
- HTTP: 293 alive / 91 gold
- HTTPS: 183 alive / 24 gold
- SOCKS4: 215 alive / 141 gold
- SOCKS5: 226 alive / 144 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29729
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

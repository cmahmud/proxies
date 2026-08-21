# SyndProxy private pool

## Current pool

- Alive now: 889
- Gold now: 403
- HTTP: 297 alive / 95 gold
- HTTPS: 151 alive / 21 gold
- SOCKS4: 218 alive / 141 gold
- SOCKS5: 223 alive / 146 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29729
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

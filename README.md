# SyndProxy private pool

## Current pool

- Alive now: 961
- Gold now: 401
- HTTP: 324 alive / 87 gold
- HTTPS: 194 alive / 26 gold
- SOCKS4: 217 alive / 142 gold
- SOCKS5: 226 alive / 146 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29729
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

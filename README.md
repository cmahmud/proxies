# SyndProxy private pool

## Current pool

- Alive now: 961
- Gold now: 292
- HTTP: 275 alive / 23 gold
- HTTPS: 190 alive / 4 gold
- SOCKS4: 250 alive / 146 gold
- SOCKS5: 246 alive / 119 gold

## Historical pool

- Discovered: 102809
- Ever alive: 12745
- Ever gold: 400

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

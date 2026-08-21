# SyndProxy private pool

## Current pool

- Alive now: 901
- Gold now: 400
- HTTP: 296 alive / 92 gold
- HTTPS: 166 alive / 21 gold
- SOCKS4: 216 alive / 142 gold
- SOCKS5: 223 alive / 145 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29729
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

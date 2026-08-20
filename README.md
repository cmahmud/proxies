# SyndProxy private pool

## Current pool

- Alive now: 1180
- Gold now: 560
- HTTP: 422 alive / 181 gold
- HTTPS: 307 alive / 94 gold
- SOCKS4: 205 alive / 129 gold
- SOCKS5: 246 alive / 156 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22949
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

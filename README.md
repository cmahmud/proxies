# SyndProxy private pool

## Current pool

- Alive now: 1045
- Gold now: 364
- HTTP: 365 alive / 81 gold
- HTTPS: 276 alive / 18 gold
- SOCKS4: 179 alive / 117 gold
- SOCKS5: 225 alive / 148 gold

## Historical pool

- Discovered: 158225
- Ever alive: 29878
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

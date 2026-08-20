# SyndProxy private pool

## Current pool

- Alive now: 746
- Gold now: 369
- HTTP: 173 alive / 76 gold
- HTTPS: 185 alive / 19 gold
- SOCKS4: 185 alive / 135 gold
- SOCKS5: 203 alive / 139 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26138
- Ever gold: 1079

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

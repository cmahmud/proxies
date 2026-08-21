# SyndProxy private pool

## Current pool

- Alive now: 946
- Gold now: 370
- HTTP: 285 alive / 81 gold
- HTTPS: 244 alive / 23 gold
- SOCKS4: 177 alive / 117 gold
- SOCKS5: 240 alive / 149 gold

## Historical pool

- Discovered: 158225
- Ever alive: 29864
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

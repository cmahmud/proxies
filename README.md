# SyndProxy private pool

## Current pool

- Alive now: 774
- Gold now: 396
- HTTP: 206 alive / 77 gold
- HTTPS: 149 alive / 28 gold
- SOCKS4: 187 alive / 134 gold
- SOCKS5: 232 alive / 157 gold

## Historical pool

- Discovered: 162241
- Ever alive: 31411
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

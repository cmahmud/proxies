# SyndProxy private pool

## Current pool

- Alive now: 1022
- Gold now: 426
- HTTP: 334 alive / 94 gold
- HTTPS: 226 alive / 23 gold
- SOCKS4: 221 alive / 159 gold
- SOCKS5: 241 alive / 150 gold

## Historical pool

- Discovered: 158252
- Ever alive: 30059
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

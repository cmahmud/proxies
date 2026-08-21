# SyndProxy private pool

## Current pool

- Alive now: 986
- Gold now: 426
- HTTP: 303 alive / 108 gold
- HTTPS: 219 alive / 27 gold
- SOCKS4: 232 alive / 153 gold
- SOCKS5: 232 alive / 138 gold

## Historical pool

- Discovered: 160020
- Ever alive: 30537
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

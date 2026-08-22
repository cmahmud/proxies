# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 406
- HTTP: 311 alive / 90 gold
- HTTPS: 258 alive / 25 gold
- SOCKS4: 225 alive / 138 gold
- SOCKS5: 242 alive / 153 gold

## Historical pool

- Discovered: 164245
- Ever alive: 32079
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

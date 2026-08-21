# SyndProxy private pool

## Current pool

- Alive now: 1083
- Gold now: 430
- HTTP: 387 alive / 84 gold
- HTTPS: 226 alive / 25 gold
- SOCKS4: 222 alive / 154 gold
- SOCKS5: 248 alive / 167 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29746
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

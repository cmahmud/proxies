# SyndProxy private pool

## Current pool

- Alive now: 908
- Gold now: 422
- HTTP: 256 alive / 93 gold
- HTTPS: 207 alive / 26 gold
- SOCKS4: 204 alive / 145 gold
- SOCKS5: 241 alive / 158 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31837
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

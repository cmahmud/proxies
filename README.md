# SyndProxy private pool

## Current pool

- Alive now: 903
- Gold now: 418
- HTTP: 254 alive / 92 gold
- HTTPS: 203 alive / 22 gold
- SOCKS4: 205 alive / 145 gold
- SOCKS5: 241 alive / 159 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31837
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

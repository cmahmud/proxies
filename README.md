# SyndProxy private pool

## Current pool

- Alive now: 872
- Gold now: 451
- HTTP: 221 alive / 106 gold
- HTTPS: 173 alive / 29 gold
- SOCKS4: 217 alive / 153 gold
- SOCKS5: 261 alive / 163 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31826
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

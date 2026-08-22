# SyndProxy private pool

## Current pool

- Alive now: 1072
- Gold now: 426
- HTTP: 336 alive / 97 gold
- HTTPS: 282 alive / 33 gold
- SOCKS4: 195 alive / 129 gold
- SOCKS5: 259 alive / 167 gold

## Historical pool

- Discovered: 161925
- Ever alive: 31177
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 421
- HTTP: 335 alive / 94 gold
- HTTPS: 262 alive / 28 gold
- SOCKS4: 199 alive / 129 gold
- SOCKS5: 252 alive / 170 gold

## Historical pool

- Discovered: 161925
- Ever alive: 31183
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

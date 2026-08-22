# SyndProxy private pool

## Current pool

- Alive now: 1058
- Gold now: 419
- HTTP: 336 alive / 93 gold
- HTTPS: 267 alive / 28 gold
- SOCKS4: 196 alive / 129 gold
- SOCKS5: 259 alive / 169 gold

## Historical pool

- Discovered: 161925
- Ever alive: 31182
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 979
- Gold now: 433
- HTTP: 295 alive / 87 gold
- HTTPS: 230 alive / 27 gold
- SOCKS4: 204 alive / 152 gold
- SOCKS5: 250 alive / 167 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31228
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

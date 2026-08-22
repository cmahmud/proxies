# SyndProxy private pool

## Current pool

- Alive now: 963
- Gold now: 432
- HTTP: 259 alive / 82 gold
- HTTPS: 240 alive / 28 gold
- SOCKS4: 212 alive / 152 gold
- SOCKS5: 252 alive / 170 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31228
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

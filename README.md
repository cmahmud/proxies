# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 434
- HTTP: 256 alive / 84 gold
- HTTPS: 239 alive / 27 gold
- SOCKS4: 207 alive / 153 gold
- SOCKS5: 249 alive / 170 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31228
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

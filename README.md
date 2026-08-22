# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 425
- HTTP: 322 alive / 87 gold
- HTTPS: 240 alive / 29 gold
- SOCKS4: 203 alive / 142 gold
- SOCKS5: 255 alive / 167 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31236
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

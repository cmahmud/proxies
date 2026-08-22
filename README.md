# SyndProxy private pool

## Current pool

- Alive now: 956
- Gold now: 428
- HTTP: 252 alive / 80 gold
- HTTPS: 239 alive / 26 gold
- SOCKS4: 210 alive / 149 gold
- SOCKS5: 255 alive / 173 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31221
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

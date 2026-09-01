# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 471
- HTTP: 139 alive / 95 gold
- HTTPS: 121 alive / 39 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 199 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46934
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

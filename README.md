# SyndProxy private pool

## Current pool

- Alive now: 940
- Gold now: 425
- HTTP: 294 alive / 89 gold
- HTTPS: 204 alive / 28 gold
- SOCKS4: 194 alive / 135 gold
- SOCKS5: 248 alive / 173 gold

## Historical pool

- Discovered: 161925
- Ever alive: 31186
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

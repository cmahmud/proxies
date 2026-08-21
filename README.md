# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 422
- HTTP: 357 alive / 106 gold
- HTTPS: 214 alive / 33 gold
- SOCKS4: 221 alive / 137 gold
- SOCKS5: 239 alive / 146 gold

## Historical pool

- Discovered: 160259
- Ever alive: 30718
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

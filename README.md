# SyndProxy private pool

## Current pool

- Alive now: 893
- Gold now: 409
- HTTP: 241 alive / 89 gold
- HTTPS: 200 alive / 19 gold
- SOCKS4: 217 alive / 151 gold
- SOCKS5: 235 alive / 150 gold

## Historical pool

- Discovered: 151674
- Ever alive: 27567
- Ever gold: 1099

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1055
- Gold now: 406
- HTTP: 357 alive / 100 gold
- HTTPS: 268 alive / 33 gold
- SOCKS4: 216 alive / 151 gold
- SOCKS5: 214 alive / 122 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30299
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

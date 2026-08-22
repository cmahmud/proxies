# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 435
- HTTP: 290 alive / 88 gold
- HTTPS: 234 alive / 28 gold
- SOCKS4: 207 alive / 151 gold
- SOCKS5: 250 alive / 168 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31229
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1082
- Gold now: 401
- HTTP: 349 alive / 106 gold
- HTTPS: 250 alive / 33 gold
- SOCKS4: 214 alive / 122 gold
- SOCKS5: 269 alive / 140 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28042
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

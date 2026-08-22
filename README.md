# SyndProxy private pool

## Current pool

- Alive now: 1066
- Gold now: 406
- HTTP: 358 alive / 89 gold
- HTTPS: 215 alive / 29 gold
- SOCKS4: 239 alive / 134 gold
- SOCKS5: 254 alive / 154 gold

## Historical pool

- Discovered: 166609
- Ever alive: 32424
- Ever gold: 1180

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

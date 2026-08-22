# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 433
- HTTP: 294 alive / 95 gold
- HTTPS: 223 alive / 27 gold
- SOCKS4: 205 alive / 143 gold
- SOCKS5: 259 alive / 168 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31246
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

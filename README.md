# SyndProxy private pool

## Current pool

- Alive now: 751
- Gold now: 404
- HTTP: 174 alive / 76 gold
- HTTPS: 129 alive / 23 gold
- SOCKS4: 224 alive / 151 gold
- SOCKS5: 224 alive / 154 gold

## Historical pool

- Discovered: 151061
- Ever alive: 27347
- Ever gold: 1095

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

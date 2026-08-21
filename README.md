# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 396
- HTTP: 317 alive / 92 gold
- HTTPS: 252 alive / 33 gold
- SOCKS4: 207 alive / 144 gold
- SOCKS5: 239 alive / 127 gold

## Historical pool

- Discovered: 160994
- Ever alive: 30913
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

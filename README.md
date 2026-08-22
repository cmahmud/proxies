# SyndProxy private pool

## Current pool

- Alive now: 947
- Gold now: 431
- HTTP: 283 alive / 96 gold
- HTTPS: 198 alive / 29 gold
- SOCKS4: 210 alive / 146 gold
- SOCKS5: 256 alive / 160 gold

## Historical pool

- Discovered: 167127
- Ever alive: 32550
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

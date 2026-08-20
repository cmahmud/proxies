# SyndProxy private pool

## Current pool

- Alive now: 1634
- Gold now: 651
- HTTP: 650 alive / 245 gold
- HTTPS: 523 alive / 121 gold
- SOCKS4: 204 alive / 127 gold
- SOCKS5: 257 alive / 158 gold

## Historical pool

- Discovered: 143486
- Ever alive: 24794
- Ever gold: 1045

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

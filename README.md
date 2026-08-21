# SyndProxy private pool

## Current pool

- Alive now: 888
- Gold now: 410
- HTTP: 287 alive / 93 gold
- HTTPS: 159 alive / 22 gold
- SOCKS4: 206 alive / 145 gold
- SOCKS5: 236 alive / 150 gold

## Historical pool

- Discovered: 152160
- Ever alive: 27817
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

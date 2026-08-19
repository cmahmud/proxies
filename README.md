# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 353
- HTTP: 310 alive / 69 gold
- HTTPS: 217 alive / 18 gold
- SOCKS4: 260 alive / 155 gold
- SOCKS5: 224 alive / 111 gold

## Historical pool

- Discovered: 110865
- Ever alive: 15982
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

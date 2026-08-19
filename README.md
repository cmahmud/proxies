# SyndProxy private pool

## Current pool

- Alive now: 980
- Gold now: 358
- HTTP: 301 alive / 69 gold
- HTTPS: 212 alive / 19 gold
- SOCKS4: 250 alive / 154 gold
- SOCKS5: 217 alive / 116 gold

## Historical pool

- Discovered: 110865
- Ever alive: 15982
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 888
- Gold now: 327
- HTTP: 300 alive / 60 gold
- HTTPS: 203 alive / 10 gold
- SOCKS4: 195 alive / 128 gold
- SOCKS5: 190 alive / 129 gold

## Historical pool

- Discovered: 129256
- Ever alive: 20141
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

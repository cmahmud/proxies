# SyndProxy private pool

## Current pool

- Alive now: 878
- Gold now: 368
- HTTP: 281 alive / 76 gold
- HTTPS: 166 alive / 20 gold
- SOCKS4: 201 alive / 128 gold
- SOCKS5: 230 alive / 144 gold

## Historical pool

- Discovered: 157406
- Ever alive: 29667
- Ever gold: 1135

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

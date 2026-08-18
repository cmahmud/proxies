# SyndProxy private pool

## Current pool

- Alive now: 527
- Gold now: 137
- HTTP: 145 alive / 31 gold
- HTTPS: 88 alive / 10 gold
- SOCKS4: 150 alive / 57 gold
- SOCKS5: 144 alive / 39 gold

## Historical pool

- Discovered: 82958
- Ever alive: 5060
- Ever gold: 259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1072
- Gold now: 472
- HTTP: 392 alive / 133 gold
- HTTPS: 250 alive / 90 gold
- SOCKS4: 218 alive / 140 gold
- SOCKS5: 212 alive / 109 gold

## Historical pool

- Discovered: 117128
- Ever alive: 17455
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

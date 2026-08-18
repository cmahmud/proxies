# SyndProxy private pool

## Current pool

- Alive now: 838
- Gold now: 284
- HTTP: 256 alive / 25 gold
- HTTPS: 117 alive / 5 gold
- SOCKS4: 245 alive / 144 gold
- SOCKS5: 220 alive / 110 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12363
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 838
- Gold now: 382
- HTTP: 250 alive / 71 gold
- HTTPS: 159 alive / 23 gold
- SOCKS4: 219 alive / 141 gold
- SOCKS5: 210 alive / 147 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25266
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

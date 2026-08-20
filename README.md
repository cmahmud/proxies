# SyndProxy private pool

## Current pool

- Alive now: 858
- Gold now: 381
- HTTP: 259 alive / 71 gold
- HTTPS: 161 alive / 22 gold
- SOCKS4: 221 alive / 141 gold
- SOCKS5: 217 alive / 147 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25266
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 548
- HTTP: 342 alive / 166 gold
- HTTPS: 237 alive / 89 gold
- SOCKS4: 231 alive / 149 gold
- SOCKS5: 210 alive / 144 gold

## Historical pool

- Discovered: 124833
- Ever alive: 19187
- Ever gold: 731

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

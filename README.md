# SyndProxy private pool

## Current pool

- Alive now: 748
- Gold now: 388
- HTTP: 178 alive / 75 gold
- HTTPS: 142 alive / 22 gold
- SOCKS4: 194 alive / 128 gold
- SOCKS5: 234 alive / 163 gold

## Historical pool

- Discovered: 150917
- Ever alive: 27081
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

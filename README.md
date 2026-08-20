# SyndProxy private pool

## Current pool

- Alive now: 1307
- Gold now: 426
- HTTP: 488 alive / 102 gold
- HTTPS: 305 alive / 26 gold
- SOCKS4: 202 alive / 141 gold
- SOCKS5: 312 alive / 157 gold

## Historical pool

- Discovered: 136246
- Ever alive: 22643
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

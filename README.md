# SyndProxy private pool

## Current pool

- Alive now: 1063
- Gold now: 532
- HTTP: 373 alive / 162 gold
- HTTPS: 244 alive / 89 gold
- SOCKS4: 223 alive / 134 gold
- SOCKS5: 223 alive / 147 gold

## Historical pool

- Discovered: 123091
- Ever alive: 18724
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1148
- Gold now: 535
- HTTP: 421 alive / 162 gold
- HTTPS: 279 alive / 90 gold
- SOCKS4: 211 alive / 138 gold
- SOCKS5: 237 alive / 145 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18627
- Ever gold: 722

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 735
- Gold now: 391
- HTTP: 160 alive / 82 gold
- HTTPS: 128 alive / 18 gold
- SOCKS4: 230 alive / 146 gold
- SOCKS5: 217 alive / 145 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25209
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 208
- HTTP: 414 alive / 24 gold
- HTTPS: 160 alive / 9 gold
- SOCKS4: 215 alive / 95 gold
- SOCKS5: 226 alive / 80 gold

## Historical pool

- Discovered: 86776
- Ever alive: 7957
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

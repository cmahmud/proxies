# SyndProxy private pool

## Current pool

- Alive now: 616
- Gold now: 208
- HTTP: 164 alive / 28 gold
- HTTPS: 94 alive / 7 gold
- SOCKS4: 182 alive / 102 gold
- SOCKS5: 176 alive / 71 gold

## Historical pool

- Discovered: 91695
- Ever alive: 8359
- Ever gold: 349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

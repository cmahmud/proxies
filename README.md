# SyndProxy private pool

## Current pool

- Alive now: 669
- Gold now: 208
- HTTP: 171 alive / 29 gold
- HTTPS: 103 alive / 7 gold
- SOCKS4: 201 alive / 100 gold
- SOCKS5: 194 alive / 72 gold

## Historical pool

- Discovered: 91695
- Ever alive: 8359
- Ever gold: 349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

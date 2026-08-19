# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 478
- HTTP: 331 alive / 120 gold
- HTTPS: 219 alive / 72 gold
- SOCKS4: 232 alive / 141 gold
- SOCKS5: 258 alive / 145 gold

## Historical pool

- Discovered: 113577
- Ever alive: 16887
- Ever gold: 626

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

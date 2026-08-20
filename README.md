# SyndProxy private pool

## Current pool

- Alive now: 1487
- Gold now: 569
- HTTP: 592 alive / 193 gold
- HTTPS: 415 alive / 86 gold
- SOCKS4: 214 alive / 129 gold
- SOCKS5: 266 alive / 161 gold

## Historical pool

- Discovered: 138843
- Ever alive: 23095
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

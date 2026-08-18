# SyndProxy private pool

## Current pool

- Alive now: 761
- Gold now: 210
- HTTP: 319 alive / 26 gold
- HTTPS: 86 alive / 9 gold
- SOCKS4: 172 alive / 95 gold
- SOCKS5: 184 alive / 80 gold

## Historical pool

- Discovered: 86776
- Ever alive: 7776
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

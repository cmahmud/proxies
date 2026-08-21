# SyndProxy private pool

## Current pool

- Alive now: 907
- Gold now: 399
- HTTP: 241 alive / 77 gold
- HTTPS: 175 alive / 23 gold
- SOCKS4: 257 alive / 159 gold
- SOCKS5: 234 alive / 140 gold

## Historical pool

- Discovered: 156830
- Ever alive: 29620
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

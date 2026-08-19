# SyndProxy private pool

## Current pool

- Alive now: 1025
- Gold now: 461
- HTTP: 364 alive / 123 gold
- HTTPS: 275 alive / 86 gold
- SOCKS4: 216 alive / 141 gold
- SOCKS5: 170 alive / 111 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17464
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

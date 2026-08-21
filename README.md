# SyndProxy private pool

## Current pool

- Alive now: 846
- Gold now: 398
- HTTP: 243 alive / 86 gold
- HTTPS: 171 alive / 19 gold
- SOCKS4: 201 alive / 134 gold
- SOCKS5: 231 alive / 159 gold

## Historical pool

- Discovered: 151681
- Ever alive: 27657
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

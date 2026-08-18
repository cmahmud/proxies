# SyndProxy private pool

## Current pool

- Alive now: 606
- Gold now: 215
- HTTP: 145 alive / 20 gold
- HTTPS: 79 alive / 9 gold
- SOCKS4: 169 alive / 101 gold
- SOCKS5: 213 alive / 85 gold

## Historical pool

- Discovered: 91002
- Ever alive: 8004
- Ever gold: 346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

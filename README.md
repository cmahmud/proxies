# SyndProxy private pool

## Current pool

- Alive now: 617
- Gold now: 216
- HTTP: 145 alive / 20 gold
- HTTPS: 79 alive / 9 gold
- SOCKS4: 179 alive / 101 gold
- SOCKS5: 214 alive / 86 gold

## Historical pool

- Discovered: 91002
- Ever alive: 8004
- Ever gold: 346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

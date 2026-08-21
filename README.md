# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 398
- HTTP: 347 alive / 107 gold
- HTTPS: 262 alive / 23 gold
- SOCKS4: 211 alive / 145 gold
- SOCKS5: 218 alive / 123 gold

## Historical pool

- Discovered: 153722
- Ever alive: 28532
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

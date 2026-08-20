# SyndProxy private pool

## Current pool

- Alive now: 763
- Gold now: 388
- HTTP: 194 alive / 77 gold
- HTTPS: 143 alive / 22 gold
- SOCKS4: 215 alive / 146 gold
- SOCKS5: 211 alive / 143 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26628
- Ever gold: 1086

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

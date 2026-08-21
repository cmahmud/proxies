# SyndProxy private pool

## Current pool

- Alive now: 1194
- Gold now: 428
- HTTP: 398 alive / 97 gold
- HTTPS: 304 alive / 25 gold
- SOCKS4: 220 alive / 145 gold
- SOCKS5: 272 alive / 161 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28210
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 924
- Gold now: 381
- HTTP: 272 alive / 72 gold
- HTTPS: 205 alive / 22 gold
- SOCKS4: 226 alive / 142 gold
- SOCKS5: 221 alive / 145 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29576
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

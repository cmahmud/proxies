# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 525
- HTTP: 351 alive / 164 gold
- HTTPS: 272 alive / 90 gold
- SOCKS4: 194 alive / 123 gold
- SOCKS5: 216 alive / 148 gold

## Historical pool

- Discovered: 124834
- Ever alive: 19192
- Ever gold: 731

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

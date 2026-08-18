# SyndProxy private pool

## Current pool

- Alive now: 614
- Gold now: 232
- HTTP: 194 alive / 30 gold
- HTTPS: 72 alive / 8 gold
- SOCKS4: 182 alive / 110 gold
- SOCKS5: 166 alive / 84 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6456
- Ever gold: 316

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

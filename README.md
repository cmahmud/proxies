# SyndProxy private pool

## Current pool

- Alive now: 748
- Gold now: 245
- HTTP: 194 alive / 28 gold
- HTTPS: 163 alive / 9 gold
- SOCKS4: 182 alive / 106 gold
- SOCKS5: 209 alive / 102 gold

## Historical pool

- Discovered: 95258
- Ever alive: 10223
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 715
- Gold now: 223
- HTTP: 194 alive / 28 gold
- HTTPS: 119 alive / 8 gold
- SOCKS4: 182 alive / 101 gold
- SOCKS5: 220 alive / 86 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8651
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

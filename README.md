# SyndProxy private pool

## Current pool

- Alive now: 994
- Gold now: 372
- HTTP: 341 alive / 92 gold
- HTTPS: 245 alive / 28 gold
- SOCKS4: 181 alive / 120 gold
- SOCKS5: 227 alive / 132 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28823
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

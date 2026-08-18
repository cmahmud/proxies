# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 308
- HTTP: 342 alive / 36 gold
- HTTPS: 221 alive / 9 gold
- SOCKS4: 215 alive / 140 gold
- SOCKS5: 233 alive / 123 gold

## Historical pool

- Discovered: 106889
- Ever alive: 14163
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

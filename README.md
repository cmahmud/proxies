# SyndProxy private pool

## Current pool

- Alive now: 1118
- Gold now: 303
- HTTP: 414 alive / 31 gold
- HTTPS: 262 alive / 4 gold
- SOCKS4: 236 alive / 140 gold
- SOCKS5: 206 alive / 128 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13421
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

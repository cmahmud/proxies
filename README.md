# SyndProxy private pool

## Current pool

- Alive now: 899
- Gold now: 249
- HTTP: 308 alive / 37 gold
- HTTPS: 221 alive / 7 gold
- SOCKS4: 233 alive / 146 gold
- SOCKS5: 137 alive / 59 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13775
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

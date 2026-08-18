# SyndProxy private pool

## Current pool

- Alive now: 941
- Gold now: 322
- HTTP: 320 alive / 41 gold
- HTTPS: 161 alive / 10 gold
- SOCKS4: 238 alive / 141 gold
- SOCKS5: 222 alive / 130 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14328
- Ever gold: 440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

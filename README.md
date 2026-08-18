# SyndProxy private pool

## Current pool

- Alive now: 937
- Gold now: 257
- HTTP: 346 alive / 34 gold
- HTTPS: 184 alive / 9 gold
- SOCKS4: 235 alive / 143 gold
- SOCKS5: 172 alive / 71 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13721
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 964
- Gold now: 260
- HTTP: 349 alive / 35 gold
- HTTPS: 203 alive / 9 gold
- SOCKS4: 233 alive / 143 gold
- SOCKS5: 179 alive / 73 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13716
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

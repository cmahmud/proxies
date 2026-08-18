# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 249
- HTTP: 324 alive / 33 gold
- HTTPS: 215 alive / 7 gold
- SOCKS4: 242 alive / 143 gold
- SOCKS5: 164 alive / 66 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13745
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

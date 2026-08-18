# SyndProxy private pool

## Current pool

- Alive now: 934
- Gold now: 250
- HTTP: 318 alive / 34 gold
- HTTPS: 214 alive / 7 gold
- SOCKS4: 239 alive / 143 gold
- SOCKS5: 163 alive / 66 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13745
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1224
- Gold now: 582
- HTTP: 397 alive / 189 gold
- HTTPS: 274 alive / 100 gold
- SOCKS4: 218 alive / 132 gold
- SOCKS5: 335 alive / 161 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23230
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

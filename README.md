# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 422
- HTTP: 316 alive / 91 gold
- HTTPS: 200 alive / 28 gold
- SOCKS4: 210 alive / 145 gold
- SOCKS5: 249 alive / 158 gold

## Historical pool

- Discovered: 162751
- Ever alive: 31553
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 745
- Gold now: 387
- HTTP: 191 alive / 82 gold
- HTTPS: 124 alive / 21 gold
- SOCKS4: 214 alive / 137 gold
- SOCKS5: 216 alive / 147 gold

## Historical pool

- Discovered: 155681
- Ever alive: 29199
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

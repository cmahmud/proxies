# SyndProxy private pool

## Current pool

- Alive now: 964
- Gold now: 323
- HTTP: 312 alive / 36 gold
- HTTPS: 186 alive / 9 gold
- SOCKS4: 241 alive / 145 gold
- SOCKS5: 225 alive / 133 gold

## Historical pool

- Discovered: 103711
- Ever alive: 14098
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

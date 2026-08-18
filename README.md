# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 320
- HTTP: 290 alive / 36 gold
- HTTPS: 174 alive / 9 gold
- SOCKS4: 229 alive / 142 gold
- SOCKS5: 218 alive / 133 gold

## Historical pool

- Discovered: 103711
- Ever alive: 14052
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

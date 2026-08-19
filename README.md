# SyndProxy private pool

## Current pool

- Alive now: 1138
- Gold now: 527
- HTTP: 427 alive / 151 gold
- HTTPS: 262 alive / 90 gold
- SOCKS4: 224 alive / 149 gold
- SOCKS5: 225 alive / 137 gold

## Historical pool

- Discovered: 119808
- Ever alive: 18033
- Ever gold: 706

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

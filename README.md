# SyndProxy private pool

## Current pool

- Alive now: 1157
- Gold now: 524
- HTTP: 438 alive / 153 gold
- HTTPS: 262 alive / 84 gold
- SOCKS4: 246 alive / 151 gold
- SOCKS5: 211 alive / 136 gold

## Historical pool

- Discovered: 119808
- Ever alive: 18007
- Ever gold: 706

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

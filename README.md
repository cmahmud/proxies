# SyndProxy private pool

## Current pool

- Alive now: 869
- Gold now: 395
- HTTP: 262 alive / 85 gold
- HTTPS: 150 alive / 22 gold
- SOCKS4: 223 alive / 142 gold
- SOCKS5: 234 alive / 146 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29723
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

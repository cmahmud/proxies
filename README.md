# SyndProxy private pool

## Current pool

- Alive now: 937
- Gold now: 280
- HTTP: 311 alive / 37 gold
- HTTPS: 223 alive / 7 gold
- SOCKS4: 240 alive / 151 gold
- SOCKS5: 163 alive / 85 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13775
- Ever gold: 429

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

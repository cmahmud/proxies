# SyndProxy private pool

## Current pool

- Alive now: 808
- Gold now: 385
- HTTP: 222 alive / 75 gold
- HTTPS: 171 alive / 23 gold
- SOCKS4: 182 alive / 125 gold
- SOCKS5: 233 alive / 162 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27141
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

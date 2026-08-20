# SyndProxy private pool

## Current pool

- Alive now: 960
- Gold now: 395
- HTTP: 301 alive / 83 gold
- HTTPS: 217 alive / 23 gold
- SOCKS4: 195 alive / 134 gold
- SOCKS5: 247 alive / 155 gold

## Historical pool

- Discovered: 144732
- Ever alive: 24966
- Ever gold: 1052

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

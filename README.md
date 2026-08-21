# SyndProxy private pool

## Current pool

- Alive now: 896
- Gold now: 416
- HTTP: 264 alive / 83 gold
- HTTPS: 176 alive / 26 gold
- SOCKS4: 218 alive / 148 gold
- SOCKS5: 238 alive / 159 gold

## Historical pool

- Discovered: 154339
- Ever alive: 28898
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

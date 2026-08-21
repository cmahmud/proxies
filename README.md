# SyndProxy private pool

## Current pool

- Alive now: 833
- Gold now: 414
- HTTP: 217 alive / 84 gold
- HTTPS: 150 alive / 24 gold
- SOCKS4: 207 alive / 142 gold
- SOCKS5: 259 alive / 164 gold

## Historical pool

- Discovered: 155796
- Ever alive: 29344
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

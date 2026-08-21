# SyndProxy private pool

## Current pool

- Alive now: 786
- Gold now: 397
- HTTP: 225 alive / 80 gold
- HTTPS: 121 alive / 17 gold
- SOCKS4: 211 alive / 150 gold
- SOCKS5: 229 alive / 150 gold

## Historical pool

- Discovered: 155789
- Ever alive: 29312
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

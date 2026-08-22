# SyndProxy private pool

## Current pool

- Alive now: 960
- Gold now: 397
- HTTP: 246 alive / 85 gold
- HTTPS: 234 alive / 25 gold
- SOCKS4: 237 alive / 137 gold
- SOCKS5: 243 alive / 150 gold

## Historical pool

- Discovered: 164253
- Ever alive: 32112
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1017
- Gold now: 397
- HTTP: 288 alive / 87 gold
- HTTPS: 234 alive / 26 gold
- SOCKS4: 233 alive / 137 gold
- SOCKS5: 262 alive / 147 gold

## Historical pool

- Discovered: 164253
- Ever alive: 32111
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 833
- Gold now: 382
- HTTP: 241 alive / 83 gold
- HTTPS: 167 alive / 24 gold
- SOCKS4: 197 alive / 128 gold
- SOCKS5: 228 alive / 147 gold

## Historical pool

- Discovered: 161996
- Ever alive: 31338
- Ever gold: 1157

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

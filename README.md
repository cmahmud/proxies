# SyndProxy private pool

## Current pool

- Alive now: 836
- Gold now: 383
- HTTP: 257 alive / 85 gold
- HTTPS: 194 alive / 26 gold
- SOCKS4: 185 alive / 128 gold
- SOCKS5: 200 alive / 144 gold

## Historical pool

- Discovered: 161996
- Ever alive: 31349
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

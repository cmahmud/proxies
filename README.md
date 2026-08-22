# SyndProxy private pool

## Current pool

- Alive now: 775
- Gold now: 343
- HTTP: 238 alive / 93 gold
- HTTPS: 150 alive / 31 gold
- SOCKS4: 164 alive / 90 gold
- SOCKS5: 223 alive / 129 gold

## Historical pool

- Discovered: 167354
- Ever alive: 32553
- Ever gold: 1188

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

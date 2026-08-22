# SyndProxy private pool

## Current pool

- Alive now: 807
- Gold now: 342
- HTTP: 247 alive / 91 gold
- HTTPS: 168 alive / 31 gold
- SOCKS4: 165 alive / 90 gold
- SOCKS5: 227 alive / 130 gold

## Historical pool

- Discovered: 167354
- Ever alive: 32554
- Ever gold: 1188

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

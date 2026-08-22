# SyndProxy private pool

## Current pool

- Alive now: 794
- Gold now: 342
- HTTP: 226 alive / 89 gold
- HTTPS: 170 alive / 31 gold
- SOCKS4: 178 alive / 93 gold
- SOCKS5: 220 alive / 129 gold

## Historical pool

- Discovered: 167354
- Ever alive: 32555
- Ever gold: 1188

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

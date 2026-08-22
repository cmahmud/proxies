# SyndProxy private pool

## Current pool

- Alive now: 829
- Gold now: 338
- HTTP: 275 alive / 97 gold
- HTTPS: 154 alive / 26 gold
- SOCKS4: 171 alive / 85 gold
- SOCKS5: 229 alive / 130 gold

## Historical pool

- Discovered: 167354
- Ever alive: 32553
- Ever gold: 1188

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 777
- Gold now: 355
- HTTP: 210 alive / 86 gold
- HTTPS: 152 alive / 28 gold
- SOCKS4: 179 alive / 104 gold
- SOCKS5: 236 alive / 137 gold

## Historical pool

- Discovered: 167354
- Ever alive: 32556
- Ever gold: 1188

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

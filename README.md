# SyndProxy private pool

## Current pool

- Alive now: 1194
- Gold now: 418
- HTTP: 403 alive / 84 gold
- HTTPS: 262 alive / 17 gold
- SOCKS4: 234 alive / 158 gold
- SOCKS5: 295 alive / 159 gold

## Historical pool

- Discovered: 134522
- Ever alive: 21871
- Ever gold: 888

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

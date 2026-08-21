# SyndProxy private pool

## Current pool

- Alive now: 1149
- Gold now: 444
- HTTP: 391 alive / 97 gold
- HTTPS: 287 alive / 32 gold
- SOCKS4: 209 alive / 147 gold
- SOCKS5: 262 alive / 168 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28719
- Ever gold: 1112

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

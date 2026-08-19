# SyndProxy private pool

## Current pool

- Alive now: 1191
- Gold now: 389
- HTTP: 396 alive / 88 gold
- HTTPS: 232 alive / 15 gold
- SOCKS4: 262 alive / 145 gold
- SOCKS5: 301 alive / 141 gold

## Historical pool

- Discovered: 133967
- Ever alive: 21715
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

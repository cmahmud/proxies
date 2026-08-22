# SyndProxy private pool

## Current pool

- Alive now: 968
- Gold now: 388
- HTTP: 301 alive / 78 gold
- HTTPS: 212 alive / 23 gold
- SOCKS4: 218 alive / 123 gold
- SOCKS5: 237 alive / 164 gold

## Historical pool

- Discovered: 164969
- Ever alive: 32246
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

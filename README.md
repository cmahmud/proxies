# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 482
- HTTP: 317 alive / 138 gold
- HTTPS: 262 alive / 92 gold
- SOCKS4: 204 alive / 138 gold
- SOCKS5: 199 alive / 114 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17340
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

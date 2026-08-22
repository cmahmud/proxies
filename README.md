# SyndProxy private pool

## Current pool

- Alive now: 1065
- Gold now: 385
- HTTP: 365 alive / 82 gold
- HTTPS: 233 alive / 24 gold
- SOCKS4: 222 alive / 124 gold
- SOCKS5: 245 alive / 155 gold

## Historical pool

- Discovered: 164970
- Ever alive: 32247
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

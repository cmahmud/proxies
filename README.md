# SyndProxy private pool

## Current pool

- Alive now: 902
- Gold now: 377
- HTTP: 284 alive / 95 gold
- HTTPS: 186 alive / 22 gold
- SOCKS4: 199 alive / 124 gold
- SOCKS5: 233 alive / 136 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29829
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

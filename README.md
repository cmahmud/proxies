# SyndProxy private pool

## Current pool

- Alive now: 948
- Gold now: 375
- HTTP: 312 alive / 90 gold
- HTTPS: 196 alive / 22 gold
- SOCKS4: 211 alive / 127 gold
- SOCKS5: 229 alive / 136 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29825
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

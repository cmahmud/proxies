# SyndProxy private pool

## Current pool

- Alive now: 1215
- Gold now: 591
- HTTP: 411 alive / 204 gold
- HTTPS: 330 alive / 101 gold
- SOCKS4: 217 alive / 137 gold
- SOCKS5: 257 alive / 149 gold

## Historical pool

- Discovered: 138948
- Ever alive: 23394
- Ever gold: 919

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

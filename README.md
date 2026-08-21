# SyndProxy private pool

## Current pool

- Alive now: 813
- Gold now: 399
- HTTP: 260 alive / 92 gold
- HTTPS: 128 alive / 20 gold
- SOCKS4: 204 alive / 141 gold
- SOCKS5: 221 alive / 146 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29729
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

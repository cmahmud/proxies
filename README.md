# SyndProxy private pool

## Current pool

- Alive now: 1062
- Gold now: 515
- HTTP: 383 alive / 157 gold
- HTTPS: 268 alive / 90 gold
- SOCKS4: 193 alive / 122 gold
- SOCKS5: 218 alive / 146 gold

## Historical pool

- Discovered: 122388
- Ever alive: 18683
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

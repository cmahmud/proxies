# SyndProxy private pool

## Current pool

- Alive now: 1059
- Gold now: 532
- HTTP: 384 alive / 160 gold
- HTTPS: 264 alive / 92 gold
- SOCKS4: 199 alive / 138 gold
- SOCKS5: 212 alive / 142 gold

## Historical pool

- Discovered: 122388
- Ever alive: 18676
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

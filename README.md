# SyndProxy private pool

## Current pool

- Alive now: 770
- Gold now: 397
- HTTP: 218 alive / 89 gold
- HTTPS: 116 alive / 22 gold
- SOCKS4: 205 alive / 135 gold
- SOCKS5: 231 alive / 151 gold

## Historical pool

- Discovered: 157428
- Ever alive: 29759
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

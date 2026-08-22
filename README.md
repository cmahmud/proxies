# SyndProxy private pool

## Current pool

- Alive now: 887
- Gold now: 397
- HTTP: 293 alive / 86 gold
- HTTPS: 152 alive / 26 gold
- SOCKS4: 213 alive / 135 gold
- SOCKS5: 229 alive / 150 gold

## Historical pool

- Discovered: 164921
- Ever alive: 32158
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

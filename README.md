# SyndProxy private pool

## Current pool

- Alive now: 1001
- Gold now: 521
- HTTP: 333 alive / 158 gold
- HTTPS: 256 alive / 87 gold
- SOCKS4: 214 alive / 141 gold
- SOCKS5: 198 alive / 135 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18469
- Ever gold: 719

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

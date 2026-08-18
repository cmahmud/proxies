# SyndProxy private pool

## Current pool

- Alive now: 864
- Gold now: 282
- HTTP: 258 alive / 27 gold
- HTTPS: 154 alive / 5 gold
- SOCKS4: 229 alive / 136 gold
- SOCKS5: 223 alive / 114 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12457
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1932
- Gold now: 700
- HTTP: 758 alive / 231 gold
- HTTPS: 603 alive / 147 gold
- SOCKS4: 235 alive / 155 gold
- SOCKS5: 336 alive / 167 gold

## Historical pool

- Discovered: 142714
- Ever alive: 24438
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1438
- Gold now: 608
- HTTP: 506 alive / 210 gold
- HTTPS: 406 alive / 113 gold
- SOCKS4: 224 alive / 149 gold
- SOCKS5: 302 alive / 136 gold

## Historical pool

- Discovered: 140466
- Ever alive: 23703
- Ever gold: 956

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 1798
- Gold now: 653
- HTTP: 688 alive / 210 gold
- HTTPS: 527 alive / 117 gold
- SOCKS4: 245 alive / 159 gold
- SOCKS5: 338 alive / 167 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24186
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy private pool

## Current pool

- Alive now: 668
- Gold now: 379
- HTTP: 174 alive / 67 gold
- HTTPS: 90 alive / 21 gold
- SOCKS4: 194 alive / 136 gold
- SOCKS5: 210 alive / 155 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25564
- Ever gold: 1065

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

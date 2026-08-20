# SyndProxy private pool

## Current pool

- Alive now: 653
- Gold now: 376
- HTTP: 167 alive / 66 gold
- HTTPS: 98 alive / 21 gold
- SOCKS4: 186 alive / 136 gold
- SOCKS5: 202 alive / 153 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25569
- Ever gold: 1065

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

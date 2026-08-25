# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 418
- HTTP: 86 alive / 61 gold
- HTTPS: 69 alive / 19 gold
- SOCKS4: 170 alive / 164 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36190
- Ever gold: 1269

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

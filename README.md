# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 418
- HTTP: 108 alive / 65 gold
- HTTPS: 95 alive / 20 gold
- SOCKS4: 182 alive / 160 gold
- SOCKS5: 201 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36037
- Ever gold: 1264

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

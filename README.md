# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 425
- HTTP: 114 alive / 78 gold
- HTTPS: 45 alive / 21 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 199 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44492
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

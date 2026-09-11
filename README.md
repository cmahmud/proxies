# SyndProxy validated proxy pool

## Current pool

- Alive now: 669
- Gold now: 346
- HTTP: 150 alive / 78 gold
- HTTPS: 86 alive / 30 gold
- SOCKS4: 160 alive / 61 gold
- SOCKS5: 273 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48574
- Ever gold: 1545

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

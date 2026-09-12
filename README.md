# SyndProxy validated proxy pool

## Current pool

- Alive now: 389
- Gold now: 316
- HTTP: 94 alive / 66 gold
- HTTPS: 33 alive / 16 gold
- SOCKS4: 120 alive / 106 gold
- SOCKS5: 142 alive / 128 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49533
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

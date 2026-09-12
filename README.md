# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 458
- HTTP: 122 alive / 96 gold
- HTTPS: 60 alive / 34 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49328
- Ever gold: 1577

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

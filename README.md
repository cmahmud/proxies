# SyndProxy validated proxy pool

## Current pool

- Alive now: 707
- Gold now: 463
- HTTP: 173 alive / 94 gold
- HTTPS: 131 alive / 34 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 230 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45304
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

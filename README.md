# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 426
- HTTP: 99 alive / 74 gold
- HTTPS: 65 alive / 26 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44430
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 409
- HTTP: 96 alive / 55 gold
- HTTPS: 69 alive / 25 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45508
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

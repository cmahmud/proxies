# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 426
- HTTP: 131 alive / 85 gold
- HTTPS: 98 alive / 30 gold
- SOCKS4: 164 alive / 152 gold
- SOCKS5: 201 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44023
- Ever gold: 1388

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 422
- HTTP: 110 alive / 68 gold
- HTTPS: 68 alive / 23 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44407
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 431
- HTTP: 103 alive / 76 gold
- HTTPS: 46 alive / 25 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44444
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

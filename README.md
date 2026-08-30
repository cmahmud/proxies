# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 428
- HTTP: 133 alive / 87 gold
- HTTPS: 100 alive / 31 gold
- SOCKS4: 164 alive / 151 gold
- SOCKS5: 201 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44023
- Ever gold: 1388

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

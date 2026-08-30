# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 422
- HTTP: 108 alive / 76 gold
- HTTPS: 50 alive / 20 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 191 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44511
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

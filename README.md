# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 444
- HTTP: 134 alive / 83 gold
- HTTPS: 64 alive / 29 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43695
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

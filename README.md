# SyndProxy validated proxy pool

## Current pool

- Alive now: 453
- Gold now: 372
- HTTP: 73 alive / 40 gold
- HTTPS: 34 alive / 11 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 178 alive / 160 gold

## Historical pool

- Discovered: 172855
- Ever alive: 32986
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

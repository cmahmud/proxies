# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 444
- HTTP: 121 alive / 81 gold
- HTTPS: 72 alive / 32 gold
- SOCKS4: 163 alive / 160 gold
- SOCKS5: 197 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44599
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

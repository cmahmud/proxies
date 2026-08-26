# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 380
- HTTP: 104 alive / 67 gold
- HTTPS: 67 alive / 18 gold
- SOCKS4: 156 alive / 144 gold
- SOCKS5: 177 alive / 151 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38790
- Ever gold: 1292

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 375
- HTTP: 115 alive / 62 gold
- HTTPS: 66 alive / 16 gold
- SOCKS4: 151 alive / 144 gold
- SOCKS5: 177 alive / 153 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38819
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

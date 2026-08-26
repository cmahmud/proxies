# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 370
- HTTP: 97 alive / 61 gold
- HTTPS: 67 alive / 15 gold
- SOCKS4: 155 alive / 143 gold
- SOCKS5: 172 alive / 151 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38839
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

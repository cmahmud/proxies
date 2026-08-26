# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 371
- HTTP: 86 alive / 61 gold
- HTTPS: 52 alive / 16 gold
- SOCKS4: 154 alive / 142 gold
- SOCKS5: 171 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38876
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

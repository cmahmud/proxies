# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 384
- HTTP: 107 alive / 64 gold
- HTTPS: 51 alive / 19 gold
- SOCKS4: 158 alive / 145 gold
- SOCKS5: 175 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38917
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

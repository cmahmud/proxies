# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 384
- HTTP: 103 alive / 69 gold
- HTTPS: 55 alive / 20 gold
- SOCKS4: 153 alive / 143 gold
- SOCKS5: 175 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38785
- Ever gold: 1292

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

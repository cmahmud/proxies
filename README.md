# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 375
- HTTP: 112 alive / 65 gold
- HTTPS: 68 alive / 15 gold
- SOCKS4: 149 alive / 143 gold
- SOCKS5: 181 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38804
- Ever gold: 1292

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

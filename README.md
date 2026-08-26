# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 424
- HTTP: 107 alive / 75 gold
- HTTPS: 89 alive / 20 gold
- SOCKS4: 186 alive / 164 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37863
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

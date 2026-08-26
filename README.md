# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 427
- HTTP: 111 alive / 75 gold
- HTTPS: 88 alive / 22 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37935
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 417
- HTTP: 90 alive / 69 gold
- HTTPS: 76 alive / 19 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 178 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37964
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

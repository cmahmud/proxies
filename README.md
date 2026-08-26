# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 419
- HTTP: 103 alive / 70 gold
- HTTPS: 87 alive / 21 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 172 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37817
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

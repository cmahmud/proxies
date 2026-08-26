# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 418
- HTTP: 101 alive / 69 gold
- HTTPS: 85 alive / 21 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 171 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37816
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

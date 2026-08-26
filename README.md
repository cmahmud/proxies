# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 425
- HTTP: 113 alive / 75 gold
- HTTPS: 90 alive / 21 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37930
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

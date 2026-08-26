# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 429
- HTTP: 105 alive / 78 gold
- HTTPS: 81 alive / 21 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 176 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37905
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

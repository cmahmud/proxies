# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 428
- HTTP: 106 alive / 77 gold
- HTTPS: 82 alive / 21 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37905
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

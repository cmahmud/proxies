# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 428
- HTTP: 104 alive / 77 gold
- HTTPS: 79 alive / 21 gold
- SOCKS4: 184 alive / 163 gold
- SOCKS5: 176 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37902
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

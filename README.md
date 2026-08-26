# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 428
- HTTP: 104 alive / 77 gold
- HTTPS: 77 alive / 20 gold
- SOCKS4: 187 alive / 164 gold
- SOCKS5: 176 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37901
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

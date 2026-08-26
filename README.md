# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 425
- HTTP: 107 alive / 75 gold
- HTTPS: 92 alive / 22 gold
- SOCKS4: 186 alive / 164 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37865
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

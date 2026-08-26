# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 402
- HTTP: 93 alive / 61 gold
- HTTPS: 75 alive / 17 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38562
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 402
- HTTP: 102 alive / 62 gold
- HTTPS: 70 alive / 17 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38699
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

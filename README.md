# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 411
- HTTP: 98 alive / 64 gold
- HTTPS: 76 alive / 20 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38634
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

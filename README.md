# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 411
- HTTP: 107 alive / 67 gold
- HTTPS: 60 alive / 20 gold
- SOCKS4: 181 alive / 159 gold
- SOCKS5: 191 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38723
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

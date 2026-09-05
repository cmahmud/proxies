# SyndProxy validated proxy pool

## Current pool

- Alive now: 376
- Gold now: 294
- HTTP: 104 alive / 77 gold
- HTTPS: 41 alive / 19 gold
- SOCKS4: 76 alive / 66 gold
- SOCKS5: 155 alive / 132 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47878
- Ever gold: 1500

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

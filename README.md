# SyndProxy validated proxy pool

## Current pool

- Alive now: 402
- Gold now: 322
- HTTP: 98 alive / 65 gold
- HTTPS: 38 alive / 22 gold
- SOCKS4: 119 alive / 104 gold
- SOCKS5: 147 alive / 131 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49519
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

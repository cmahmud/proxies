# SyndProxy validated proxy pool

## Current pool

- Alive now: 386
- Gold now: 328
- HTTP: 80 alive / 66 gold
- HTTPS: 30 alive / 19 gold
- SOCKS4: 132 alive / 115 gold
- SOCKS5: 144 alive / 128 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49547
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

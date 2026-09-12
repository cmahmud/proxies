# SyndProxy validated proxy pool

## Current pool

- Alive now: 408
- Gold now: 320
- HTTP: 98 alive / 67 gold
- HTTPS: 43 alive / 19 gold
- SOCKS4: 127 alive / 107 gold
- SOCKS5: 140 alive / 127 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49545
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

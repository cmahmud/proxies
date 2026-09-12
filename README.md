# SyndProxy validated proxy pool

## Current pool

- Alive now: 389
- Gold now: 320
- HTTP: 89 alive / 68 gold
- HTTPS: 35 alive / 20 gold
- SOCKS4: 128 alive / 105 gold
- SOCKS5: 137 alive / 127 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49539
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

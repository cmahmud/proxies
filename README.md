# SyndProxy validated proxy pool

## Current pool

- Alive now: 392
- Gold now: 332
- HTTP: 84 alive / 65 gold
- HTTPS: 33 alive / 18 gold
- SOCKS4: 130 alive / 116 gold
- SOCKS5: 145 alive / 133 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49548
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

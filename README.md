# SyndProxy validated proxy pool

## Current pool

- Alive now: 394
- Gold now: 318
- HTTP: 91 alive / 67 gold
- HTTPS: 37 alive / 19 gold
- SOCKS4: 129 alive / 105 gold
- SOCKS5: 137 alive / 127 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49537
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

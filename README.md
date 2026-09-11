# SyndProxy validated proxy pool

## Current pool

- Alive now: 417
- Gold now: 353
- HTTP: 109 alive / 80 gold
- HTTPS: 47 alive / 26 gold
- SOCKS4: 81 alive / 74 gold
- SOCKS5: 180 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48663
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 445
- Gold now: 370
- HTTP: 117 alive / 90 gold
- HTTPS: 38 alive / 29 gold
- SOCKS4: 86 alive / 76 gold
- SOCKS5: 204 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48647
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

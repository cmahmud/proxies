# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 467
- HTTP: 138 alive / 97 gold
- HTTPS: 58 alive / 33 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 193 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49350
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

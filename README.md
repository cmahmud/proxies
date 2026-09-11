# SyndProxy validated proxy pool

## Current pool

- Alive now: 423
- Gold now: 348
- HTTP: 111 alive / 77 gold
- HTTPS: 51 alive / 25 gold
- SOCKS4: 80 alive / 74 gold
- SOCKS5: 181 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48664
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

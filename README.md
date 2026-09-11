# SyndProxy validated proxy pool

## Current pool

- Alive now: 425
- Gold now: 354
- HTTP: 111 alive / 81 gold
- HTTPS: 50 alive / 27 gold
- SOCKS4: 81 alive / 75 gold
- SOCKS5: 183 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48656
- Ever gold: 1563

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

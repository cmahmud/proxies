# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 438
- HTTP: 105 alive / 77 gold
- HTTPS: 58 alive / 27 gold
- SOCKS4: 189 alive / 164 gold
- SOCKS5: 179 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49123
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

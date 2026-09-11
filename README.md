# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 437
- HTTP: 110 alive / 77 gold
- HTTPS: 55 alive / 26 gold
- SOCKS4: 190 alive / 170 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49109
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

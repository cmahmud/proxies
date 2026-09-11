# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 438
- HTTP: 109 alive / 77 gold
- HTTPS: 52 alive / 28 gold
- SOCKS4: 187 alive / 165 gold
- SOCKS5: 174 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49117
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

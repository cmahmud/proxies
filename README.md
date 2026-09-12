# SyndProxy validated proxy pool

## Current pool

- Alive now: 431
- Gold now: 358
- HTTP: 92 alive / 69 gold
- HTTPS: 32 alive / 17 gold
- SOCKS4: 146 alive / 126 gold
- SOCKS5: 161 alive / 146 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49553
- Ever gold: 1586

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

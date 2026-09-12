# SyndProxy validated proxy pool

## Current pool

- Alive now: 438
- Gold now: 348
- HTTP: 95 alive / 64 gold
- HTTPS: 37 alive / 17 gold
- SOCKS4: 146 alive / 123 gold
- SOCKS5: 160 alive / 144 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49553
- Ever gold: 1586

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

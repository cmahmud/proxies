# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 454
- HTTP: 124 alive / 95 gold
- HTTPS: 59 alive / 31 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49327
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

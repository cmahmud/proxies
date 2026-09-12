# SyndProxy validated proxy pool

## Current pool

- Alive now: 379
- Gold now: 304
- HTTP: 83 alive / 59 gold
- HTTPS: 33 alive / 12 gold
- SOCKS4: 116 alive / 107 gold
- SOCKS5: 147 alive / 126 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49487
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 380
- Gold now: 321
- HTTP: 81 alive / 64 gold
- HTTPS: 34 alive / 21 gold
- SOCKS4: 117 alive / 108 gold
- SOCKS5: 148 alive / 128 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49487
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

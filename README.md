# SyndProxy validated proxy pool

## Current pool

- Alive now: 407
- Gold now: 320
- HTTP: 97 alive / 66 gold
- HTTPS: 44 alive / 19 gold
- SOCKS4: 126 alive / 107 gold
- SOCKS5: 140 alive / 128 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49545
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

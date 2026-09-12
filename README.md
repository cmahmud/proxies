# SyndProxy validated proxy pool

## Current pool

- Alive now: 360
- Gold now: 310
- HTTP: 79 alive / 59 gold
- HTTPS: 34 alive / 20 gold
- SOCKS4: 111 alive / 103 gold
- SOCKS5: 136 alive / 128 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49501
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

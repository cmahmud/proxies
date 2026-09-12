# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 423
- HTTP: 103 alive / 77 gold
- HTTPS: 52 alive / 23 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 174 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49452
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

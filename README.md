# SyndProxy validated proxy pool

## Current pool

- Alive now: 389
- Gold now: 313
- HTTP: 88 alive / 64 gold
- HTTPS: 36 alive / 16 gold
- SOCKS4: 121 alive / 104 gold
- SOCKS5: 144 alive / 129 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49527
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

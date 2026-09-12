# SyndProxy validated proxy pool

## Current pool

- Alive now: 386
- Gold now: 313
- HTTP: 87 alive / 63 gold
- HTTPS: 35 alive / 16 gold
- SOCKS4: 122 alive / 105 gold
- SOCKS5: 142 alive / 129 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49527
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

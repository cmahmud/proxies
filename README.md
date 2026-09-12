# SyndProxy validated proxy pool

## Current pool

- Alive now: 392
- Gold now: 317
- HTTP: 87 alive / 64 gold
- HTTPS: 33 alive / 21 gold
- SOCKS4: 122 alive / 103 gold
- SOCKS5: 150 alive / 129 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49521
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

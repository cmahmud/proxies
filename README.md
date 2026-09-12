# SyndProxy validated proxy pool

## Current pool

- Alive now: 389
- Gold now: 314
- HTTP: 91 alive / 65 gold
- HTTPS: 33 alive / 16 gold
- SOCKS4: 122 alive / 105 gold
- SOCKS5: 143 alive / 128 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49531
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

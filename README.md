# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 419
- HTTP: 102 alive / 74 gold
- HTTPS: 50 alive / 20 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49480
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 420
- HTTP: 103 alive / 74 gold
- HTTPS: 47 alive / 20 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49480
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

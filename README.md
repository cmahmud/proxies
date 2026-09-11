# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 419
- HTTP: 103 alive / 67 gold
- HTTPS: 47 alive / 20 gold
- SOCKS4: 196 alive / 162 gold
- SOCKS5: 178 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48880
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

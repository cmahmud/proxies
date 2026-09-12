# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 468
- HTTP: 133 alive / 96 gold
- HTTPS: 60 alive / 35 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49353
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

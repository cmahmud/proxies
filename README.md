# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 470
- HTTP: 132 alive / 97 gold
- HTTPS: 58 alive / 35 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 194 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49355
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

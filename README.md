# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 430
- HTTP: 90 alive / 70 gold
- HTTPS: 104 alive / 32 gold
- SOCKS4: 178 alive / 158 gold
- SOCKS5: 181 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47313
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 446
- HTTP: 96 alive / 76 gold
- HTTPS: 99 alive / 30 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 190 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47350
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

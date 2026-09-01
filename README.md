# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 421
- HTTP: 92 alive / 67 gold
- HTTPS: 73 alive / 26 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47071
- Ever gold: 1464

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

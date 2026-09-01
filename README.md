# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 425
- HTTP: 87 alive / 67 gold
- HTTPS: 58 alive / 27 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47069
- Ever gold: 1464

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

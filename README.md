# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 402
- HTTP: 73 alive / 53 gold
- HTTPS: 51 alive / 19 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47105
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

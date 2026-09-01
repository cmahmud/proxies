# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 411
- HTTP: 84 alive / 55 gold
- HTTPS: 53 alive / 24 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47100
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

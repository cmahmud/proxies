# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 412
- HTTP: 86 alive / 55 gold
- HTTPS: 55 alive / 24 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 180 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47100
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

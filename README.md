# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 420
- HTTP: 83 alive / 63 gold
- HTTPS: 43 alive / 24 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 181 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47088
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

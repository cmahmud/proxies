# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 420
- HTTP: 85 alive / 62 gold
- HTTPS: 68 alive / 25 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47123
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 375
- HTTP: 106 alive / 52 gold
- HTTPS: 35 alive / 12 gold
- SOCKS4: 175 alive / 154 gold
- SOCKS5: 193 alive / 157 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33035
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

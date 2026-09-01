# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 417
- HTTP: 84 alive / 61 gold
- HTTPS: 53 alive / 24 gold
- SOCKS4: 170 alive / 164 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47074
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

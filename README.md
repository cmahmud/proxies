# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 409
- HTTP: 77 alive / 62 gold
- HTTPS: 99 alive / 23 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 175 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47206
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

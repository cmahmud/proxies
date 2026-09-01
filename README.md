# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 420
- HTTP: 82 alive / 60 gold
- HTTPS: 41 alive / 26 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 179 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47092
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 424
- HTTP: 86 alive / 69 gold
- HTTPS: 97 alive / 30 gold
- SOCKS4: 178 alive / 157 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47288
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

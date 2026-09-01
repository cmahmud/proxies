# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 464
- HTTP: 128 alive / 90 gold
- HTTPS: 110 alive / 35 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 193 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46350
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

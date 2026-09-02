# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 444
- HTTP: 91 alive / 73 gold
- HTTPS: 104 alive / 32 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 189 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47443
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

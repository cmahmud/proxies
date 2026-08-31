# SyndProxy validated proxy pool

## Current pool

- Alive now: 661
- Gold now: 459
- HTTP: 135 alive / 91 gold
- HTTPS: 131 alive / 31 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 223 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46061
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

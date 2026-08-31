# SyndProxy validated proxy pool

## Current pool

- Alive now: 679
- Gold now: 458
- HTTP: 141 alive / 91 gold
- HTTPS: 140 alive / 30 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 226 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46067
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

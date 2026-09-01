# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 449
- HTTP: 101 alive / 77 gold
- HTTPS: 107 alive / 31 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 191 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47420
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

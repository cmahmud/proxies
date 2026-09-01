# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 445
- HTTP: 92 alive / 77 gold
- HTTPS: 102 alive / 32 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 191 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47349
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

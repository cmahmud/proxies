# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 477
- HTTP: 141 alive / 98 gold
- HTTPS: 131 alive / 40 gold
- SOCKS4: 184 alive / 164 gold
- SOCKS5: 198 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46949
- Ever gold: 1458

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

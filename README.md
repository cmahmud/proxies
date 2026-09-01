# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 426
- HTTP: 83 alive / 68 gold
- HTTPS: 92 alive / 31 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47314
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

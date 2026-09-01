# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 418
- HTTP: 91 alive / 66 gold
- HTTPS: 67 alive / 24 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47071
- Ever gold: 1464

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

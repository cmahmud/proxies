# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 426
- HTTP: 101 alive / 69 gold
- HTTPS: 65 alive / 27 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47068
- Ever gold: 1464

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

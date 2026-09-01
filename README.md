# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 454
- HTTP: 127 alive / 84 gold
- HTTPS: 126 alive / 29 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 192 alive / 181 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46784
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

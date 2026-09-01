# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 448
- HTTP: 96 alive / 77 gold
- HTTPS: 97 alive / 33 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 193 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47392
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

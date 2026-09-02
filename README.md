# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 440
- HTTP: 97 alive / 73 gold
- HTTPS: 95 alive / 29 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 190 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47444
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

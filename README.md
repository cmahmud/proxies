# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 435
- HTTP: 125 alive / 77 gold
- HTTPS: 96 alive / 21 gold
- SOCKS4: 187 alive / 162 gold
- SOCKS5: 193 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47574
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

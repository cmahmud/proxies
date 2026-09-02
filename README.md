# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 440
- HTTP: 109 alive / 79 gold
- HTTPS: 96 alive / 23 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 184 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47589
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

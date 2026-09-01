# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 461
- HTTP: 146 alive / 93 gold
- HTTPS: 122 alive / 33 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 194 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46878
- Ever gold: 1453

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

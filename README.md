# SyndProxy validated proxy pool

## Current pool

- Alive now: 686
- Gold now: 461
- HTTP: 148 alive / 93 gold
- HTTPS: 143 alive / 33 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 221 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46097
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

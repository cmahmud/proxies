# SyndProxy validated proxy pool

## Current pool

- Alive now: 695
- Gold now: 460
- HTTP: 142 alive / 88 gold
- HTTPS: 143 alive / 36 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 229 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45847
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

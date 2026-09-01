# SyndProxy validated proxy pool

## Current pool

- Alive now: 664
- Gold now: 472
- HTTP: 150 alive / 95 gold
- HTTPS: 127 alive / 40 gold
- SOCKS4: 185 alive / 163 gold
- SOCKS5: 202 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46957
- Ever gold: 1461

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

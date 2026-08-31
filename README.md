# SyndProxy validated proxy pool

## Current pool

- Alive now: 664
- Gold now: 472
- HTTP: 163 alive / 102 gold
- HTTPS: 128 alive / 34 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 196 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45175
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

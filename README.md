# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 381
- HTTP: 102 alive / 64 gold
- HTTPS: 101 alive / 14 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 181 alive / 146 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43042
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

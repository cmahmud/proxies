# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 490
- HTTP: 143 alive / 101 gold
- HTTPS: 136 alive / 47 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 198 alive / 179 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44994
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

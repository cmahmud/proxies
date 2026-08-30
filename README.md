# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 443
- HTTP: 118 alive / 79 gold
- HTTPS: 114 alive / 35 gold
- SOCKS4: 163 alive / 159 gold
- SOCKS5: 195 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44643
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

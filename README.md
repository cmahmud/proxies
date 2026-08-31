# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 481
- HTTP: 148 alive / 98 gold
- HTTPS: 127 alive / 46 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 194 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45027
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

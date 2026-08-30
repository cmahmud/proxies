# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 424
- HTTP: 126 alive / 83 gold
- HTTPS: 65 alive / 27 gold
- SOCKS4: 156 alive / 151 gold
- SOCKS5: 183 alive / 163 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43696
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

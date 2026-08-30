# SyndProxy validated proxy pool

## Current pool

- Alive now: 659
- Gold now: 487
- HTTP: 162 alive / 101 gold
- HTTPS: 128 alive / 45 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 198 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44991
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

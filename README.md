# SyndProxy validated proxy pool

## Current pool

- Alive now: 665
- Gold now: 472
- HTTP: 163 alive / 101 gold
- HTTPS: 128 alive / 35 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45177
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

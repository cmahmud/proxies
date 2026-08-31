# SyndProxy validated proxy pool

## Current pool

- Alive now: 664
- Gold now: 481
- HTTP: 162 alive / 101 gold
- HTTPS: 135 alive / 42 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 197 alive / 179 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45221
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

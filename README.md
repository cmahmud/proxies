# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 481
- HTTP: 147 alive / 101 gold
- HTTPS: 129 alive / 42 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 195 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44947
- Ever gold: 1420

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

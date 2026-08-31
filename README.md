# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 474
- HTTP: 142 alive / 101 gold
- HTTPS: 121 alive / 36 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 195 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45179
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

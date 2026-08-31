# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 474
- HTTP: 153 alive / 101 gold
- HTTPS: 123 alive / 36 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45177
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

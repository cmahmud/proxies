# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 477
- HTTP: 163 alive / 101 gold
- HTTPS: 123 alive / 37 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 193 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45191
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

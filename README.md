# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 474
- HTTP: 157 alive / 99 gold
- HTTPS: 115 alive / 37 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 194 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45191
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

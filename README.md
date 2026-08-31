# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 481
- HTTP: 154 alive / 103 gold
- HTTPS: 132 alive / 39 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 194 alive / 179 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45226
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

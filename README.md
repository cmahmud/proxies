# SyndProxy validated proxy pool

## Current pool

- Alive now: 666
- Gold now: 480
- HTTP: 161 alive / 100 gold
- HTTPS: 134 alive / 42 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 200 alive / 179 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45221
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

# SyndProxy validated proxy pool

## Current pool

- Alive now: 666
- Gold now: 480
- HTTP: 148 alive / 107 gold
- HTTPS: 151 alive / 37 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 195 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45230
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

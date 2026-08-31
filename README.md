# SyndProxy validated proxy pool

## Current pool

- Alive now: 664
- Gold now: 481
- HTTP: 147 alive / 107 gold
- HTTPS: 155 alive / 37 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 193 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45230
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

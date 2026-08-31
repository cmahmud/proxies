# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 419
- HTTP: 112 alive / 67 gold
- HTTPS: 66 alive / 21 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 205 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45520
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

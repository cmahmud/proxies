# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 419
- HTTP: 116 alive / 68 gold
- HTTPS: 72 alive / 20 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 205 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45521
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

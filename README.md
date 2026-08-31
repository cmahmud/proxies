# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 421
- HTTP: 111 alive / 69 gold
- HTTPS: 75 alive / 22 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 201 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45521
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

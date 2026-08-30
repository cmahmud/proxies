# SyndProxy validated proxy pool

## Current pool

- Alive now: 669
- Gold now: 481
- HTTP: 157 alive / 99 gold
- HTTPS: 142 alive / 44 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 201 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44968
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

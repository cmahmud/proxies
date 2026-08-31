# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 437
- HTTP: 143 alive / 75 gold
- HTTPS: 103 alive / 29 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 209 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45395
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

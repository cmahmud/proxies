# SyndProxy validated proxy pool

## Current pool

- Alive now: 658
- Gold now: 473
- HTTP: 157 alive / 102 gold
- HTTPS: 134 alive / 37 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45231
- Ever gold: 1427

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

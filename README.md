# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 454
- HTTP: 129 alive / 87 gold
- HTTPS: 72 alive / 34 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 197 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45568
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

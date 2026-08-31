# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 458
- HTTP: 123 alive / 86 gold
- HTTPS: 113 alive / 36 gold
- SOCKS4: 174 alive / 164 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45626
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

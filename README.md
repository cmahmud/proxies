# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 457
- HTTP: 122 alive / 86 gold
- HTTPS: 109 alive / 36 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45626
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.

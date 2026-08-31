# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 437
- HTTP: 144 alive / 73 gold
- HTTPS: 102 alive / 30 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 209 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45395
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
